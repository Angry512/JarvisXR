from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "preview" / "windows_jarvis_preview" / "jarvis_preview.py"
IOS_ROOT = ROOT / "ios" / "JarvisXR" / "JarvisXR"


def load_preview_module():
    spec = importlib.util.spec_from_file_location("jarvis_preview", PREVIEW)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load preview module.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    preview = load_preview_module()
    root = read(IOS_ROOT / "JarvisRootViewController.swift")
    help_swift = read(IOS_ROOT / "JarvisHelpViewController.swift")
    router = read(IOS_ROOT / "JarvisCommandRouter.swift")
    planner = read(IOS_ROOT / "JarvisCommandPlan.swift")
    mesh = read(IOS_ROOT / "JarvisControlMeshPlanner.swift")
    camera = read(IOS_ROOT / "JarvisCameraViewController.swift")
    vision = read(IOS_ROOT / "JarvisVisionInterfaces.swift")
    preview_text = read(PREVIEW)
    voice = read(IOS_ROOT / "JarvisVoiceInputService.swift")
    state = read(IOS_ROOT / "JarvisInteractionState.swift")
    info_plist = read(IOS_ROOT / "Info.plist")
    project_yml = read(ROOT / "ios" / "JarvisXR" / "project.yml")

    failures: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            failures.append(name)

    model = preview.InteractionModel()
    initial_surface = "\n".join(model.product_surface_texts())
    model.open_help()
    help_surface = "\n".join(model.product_surface_texts())
    model.close_help()
    model.open_mesh()
    mesh_surface = "\n".join(model.product_surface_texts())

    check("Swift help button exists", 'setTitle("?",' in root)
    check("Swift Mesh button exists", 'setTitle("Mesh"' in root)
    check("Preview exposes product-only mode", "--product-only" in preview_text and "Product-only view" in preview_text)
    check("Preview has Mesh sheet", "Control Mesh" in mesh_surface and "Voice Control" in mesh_surface)
    check("Help includes scan read detect Mesh", all(term in help_swift for term in ["scan this", "read this", "detect objects", "Control Mesh"]))
    check("Help avoids forbidden words", all(term not in help_swift.lower() for term in ["json", "debug", "approval gate", "test step"]))
    check("Phone surface avoids JSON", "JSON" not in initial_surface and "json" not in initial_surface.lower())
    check("Phone surface avoids guide/checklist text", all(term not in initial_surface.lower() for term in ["checklist", "approval", "should say ready"]))
    check("Keyboard keeps required controls", _keyboard_ok(preview))
    check("Orb flow works", _orb_flow_ok(preview))
    check("Speaking tap stops", _speaking_stop_ok(preview))
    check("Permission denied state exists", _state_contains(preview, "permission_denied", "permission"))
    check("No speech state exists", _state_contains(preview, "no_speech", "No speech heard"))
    check("Scan routes to inspection", preview.InteractionModel().process("scan this").state == "Inspection")
    check("Read routes to OCR", preview.InteractionModel().process("read this").action == "ocr")
    detect = preview.InteractionModel().process("detect objects")
    check("Detect objects routes and is model gated", detect.state == "Inspection" and "model" in detect.display.lower())
    check("Go home routes to Control Mesh", preview.InteractionModel().process("go home").action == "control_mesh")
    check("Tap routes to grid", "show grid" in preview.InteractionModel().process("tap that").display.lower())
    check("Return route exists", "jarvis://standby" in mesh and "return to jarvis" in mesh.lower())
    check("Object detection is model gated", "Object model not installed" in vision and "VNCoreMLModel" in vision)
    check("No Recent Activity in product sources", "Recent Activity" not in root)
    check("No response panel label", "JARVIS RESPONSE" not in root)
    check("No debug chips", all(term not in root for term in ["Wi-Fi path available", "offline tools remain", "guided ready"]))
    check("No product-facing XR in root", "XR" not in root.replace("JarvisXRLayoutModel", "").replace("iPhone XR keyboard", ""))
    check("No WebView stack", all(term not in root + help_swift + router + camera for term in ["WebView", "WKWebView"]))
    check("No private implementation strings", all(term not in root + router + camera for term in ["UIApplication.shared.perform", "LSApplicationWorkspace", "SpringBoardServices"]))
    check("Tap and long press are separate recognizers", "UITapGestureRecognizer" in root and "UILongPressGestureRecognizer" in root and "tap.require(toFail: longPress)" in root)
    check("Long press returns standby", "enterStandbyFromLongPress" in root and "voiceInput.stopListening(process: false)" in root)
    check("Manual listening stop processes transcript", "voiceInput.stopListening(process: true)" in root and "onFinalTranscript" in voice)
    check("No speech returns ready", "case .noSpeech:" in root and "setInterfaceState(.ready, hint: \"No speech heard.\")" in root)
    check("Real UIKit layout uses keyboardLayoutGuide", "keyboardLayoutGuide.topAnchor" in root and "keyboardWillChangeFrameNotification" not in root)
    check("Real UIKit source avoids copied preview layout model", "JarvisXRLayoutModel" not in root + state)
    check("Launch screen configured", "UILaunchStoryboardName" in info_plist and "LaunchScreen" in info_plist and "LaunchScreen.storyboard" in project_yml)
    check("Markdown model notes excluded from app bundle", "Models/README.md" in project_yml)
    check("No primary Spotify music example", "Try: open Spotify" not in root + help_swift + preview_text and "play music" not in help_swift)

    if failures:
        print("JARVIS product surface test failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("JARVIS product surface test passed:")
    print("- Swift help and Mesh controls exist")
    print("- Help, Mesh, preview, planner, vision, and routing checks passed")
    print("- Product surface avoids forbidden debug/report UI")
    return 0


def _keyboard_ok(preview) -> bool:
    model = preview.InteractionModel()
    model.toggle_keyboard()
    layout = model.layout()
    return (
        layout.compact
        and layout.input_top + preview.INPUT_HEIGHT < preview.PHONE_HEIGHT - preview.SAFE_BOTTOM - preview.KEYBOARD_HEIGHT
        and layout.help_bounds[1] >= preview.SAFE_TOP
        and layout.menu_bounds[1] >= preview.SAFE_TOP
    )


def _orb_flow_ok(preview) -> bool:
    model = preview.InteractionModel()
    return model.orb_tap() == "JARVIS ready" and model.orb_tap() == "Listening" and model.orb_tap() in {"Inspection", "Done", "JARVIS ready"}


def _speaking_stop_ok(preview) -> bool:
    model = preview.InteractionModel()
    model.speaking()
    return model.orb_tap() == "JARVIS ready"


def _state_contains(preview, method_name: str, expected: str) -> bool:
    model = preview.InteractionModel()
    getattr(model, method_name)()
    return expected.lower() in "\n".join(model.product_surface_texts()).lower()


if __name__ == "__main__":
    raise SystemExit(main())
