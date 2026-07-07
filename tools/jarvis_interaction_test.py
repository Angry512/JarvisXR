from __future__ import annotations

import importlib.util
import sys
import datetime as dt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "preview" / "windows_jarvis_preview" / "jarvis_preview.py"
BUNDLE = ROOT / "dist" / "jarvis_local_approval_bundle"
REPORT = BUNDLE / "latest_test_report.txt"
IOS_ROOT = ROOT / "ios" / "JarvisXR" / "JarvisXR"


def load_preview_module():
    spec = importlib.util.spec_from_file_location("jarvis_preview", PREVIEW)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load Windows preview module.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    preview = load_preview_module()
    model = preview.InteractionModel()
    failures: list[str] = []
    passed: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            failures.append(name)
        else:
            passed.append(name)

    surface_text = "\n".join(model.product_surface_texts()).lower()
    swift_root = (IOS_ROOT / "JarvisRootViewController.swift").read_text(encoding="utf-8")
    swift_help = (IOS_ROOT / "JarvisHelpViewController.swift").read_text(encoding="utf-8")
    swift_voice = (IOS_ROOT / "JarvisVoiceInputService.swift").read_text(encoding="utf-8")
    swift_state = (IOS_ROOT / "JarvisInteractionState.swift").read_text(encoding="utf-8")
    swift_router = (IOS_ROOT / "JarvisCommandRouter.swift").read_text(encoding="utf-8")
    swift_planner = (IOS_ROOT / "JarvisCommandPlan.swift").read_text(encoding="utf-8")
    swift_mesh = (IOS_ROOT / "JarvisControlMeshPlanner.swift").read_text(encoding="utf-8")
    swift_vision = (IOS_ROOT / "JarvisVisionInterfaces.swift").read_text(encoding="utf-8")
    info_plist = (IOS_ROOT / "Info.plist").read_text(encoding="utf-8")
    project_yml = (ROOT / "ios" / "JarvisXR" / "project.yml").read_text(encoding="utf-8")

    check("help icon model exists", hasattr(model, "open_help"))
    check("help icon exists in iOS source", 'setTitle("?",' in swift_root)
    check("mesh control is understandable in iOS source", 'setTitle("Mesh"' in swift_root and "Control Mesh and systems" in swift_root)
    check("planner source exists", "JarvisCommandPlan" in swift_planner and "JarvisCapabilityRoute" in swift_planner)
    check("control mesh planner source exists", "JarvisControlMeshPlanner" in swift_mesh)
    check("initial surface has no guide text", "should " + "say ready" not in surface_text and "approval" not in surface_text)
    check("initial surface has no product data dump", "debug" not in surface_text and "export" not in surface_text)
    check("no Recent Activity in product Swift", "Recent Activity" not in swift_root)
    check("no response panel label in product Swift", "JARVIS RESPONSE" not in swift_root)
    check("no debug chips in product Swift", "Wi-Fi path available" not in swift_root and "offline tools remain" not in swift_root and "guided ready" not in swift_root)

    standby_model = preview.InteractionModel()
    check("tap_from_standby_enters_ready_not_listening", standby_model.orb_tap() == "JARVIS ready")
    check("tap_from_ready_starts_listening", standby_model.orb_tap() == "Listening")
    standby_model.simulate_partial("status")
    before_endpoint = standby_model.state
    response = standby_model.orb_tap()
    check("tap_from_listening_processes_transcript_not_standby", before_endpoint == "Listening" and response != "Standby" and standby_model.state != "Standby")

    scan_model = preview.InteractionModel()
    scan_model.orb_tap()
    scan_model.orb_tap()
    scan_model.simulate_partial("scan this")
    check("tap_from_listening_with_scan_routes_inspection", scan_model.orb_tap() == "Inspection")

    read_model = preview.InteractionModel()
    read_model.orb_tap()
    read_model.orb_tap()
    read_model.simulate_partial("read this")
    read_response = read_model.endpoint()
    check("tap_from_listening_with_read_routes_ocr_or_inspection", read_response.action == "ocr" and read_model.state == "Inspection")

    detect_model = preview.InteractionModel()
    detect_model.orb_tap()
    detect_model.orb_tap()
    detect_model.simulate_partial("detect objects")
    detect_response_from_voice = detect_model.endpoint()
    check("tap_from_listening_with_detect_routes_inspection_model_gated", detect_response_from_voice.action == "object_model_missing" and detect_model.state == "Inspection")

    empty_model = preview.InteractionModel()
    empty_model.orb_tap()
    empty_model.orb_tap()
    check("listening_tap_with_empty_transcript_returns_no_speech_then_ready", empty_model.orb_tap() == "JARVIS ready" and "no speech" in empty_model.last_response.lower())

    hold_ready = preview.InteractionModel()
    hold_ready.orb_tap()
    check("long_hold_from_ready_enters_standby", hold_ready.pointer_up(after_seconds=preview.LONG_HOLD_SECONDS) == "Standby")

    hold_listening = preview.InteractionModel()
    hold_listening.orb_tap()
    hold_listening.orb_tap()
    hold_listening.simulate_partial("scan this")
    check("long_hold_from_listening_cancels_without_processing_and_enters_standby", hold_listening.pointer_up(after_seconds=preview.LONG_HOLD_SECONDS) == "Standby" and hold_listening.partial_transcript == "")

    hold_speaking = preview.InteractionModel()
    hold_speaking.speaking()
    check("long_hold_from_speaking_stops_speech_and_enters_standby", hold_speaking.pointer_up(after_seconds=preview.LONG_HOLD_SECONDS) == "Standby")

    no_tap_after_hold = preview.InteractionModel()
    no_tap_after_hold.orb_tap()
    no_tap_after_hold.pointer_down()
    released_state = no_tap_after_hold.pointer_up(after_seconds=preview.LONG_HOLD_SECONDS)
    after_release_state = no_tap_after_hold.state
    check("long_hold_does_not_trigger_tap_on_release", released_state == "Standby" and after_release_state == "Standby")

    normal_tap_states = []
    normal_tap = preview.InteractionModel()
    for _ in range(4):
        normal_tap_states.append(normal_tap.orb_tap())
    check("normal_tap_never_enters_standby", "Standby" not in normal_tap_states)

    typed_response = preview.InteractionModel().process("scan this")
    check("typed_command_still_routes", typed_response.action == "inspect" and typed_response.state == "Inspection")

    help_lower = swift_help.lower()
    check("help_text_contains_correct_tap_hold_sequence", all(term in help_lower for term in ["tap once from standby", "tap again to listen", "tap while listening to process", "long hold the orb"]))
    check("Swift source has UILongPressGestureRecognizer", "UILongPressGestureRecognizer" in swift_root and "minimumPressDuration = 0.72" in swift_root)
    check("Swift tap waits for long press failure", "tap.require(toFail: longPress)" in swift_root)
    check("Swift root does not call standby from normal listening stop", "case .listening, .heardYou:\n            voiceInput.stopListening(process: true)" in swift_root and "case .processing:\n            showTransient(\"Processing.\")" in swift_root)
    check("Voice service supports process and cancel stop modes", "func stopListening(process: Bool = true)" in swift_voice and "finishRecognition(process: process)" in swift_voice)
    check("Voice no speech does not force standby", "self.onStateChange?(.noSpeech)\n                self.onStateChange?(.standby)" not in swift_voice)
    check("LaunchScreen configured in Info.plist/project.yml", "UILaunchStoryboardName" in info_plist and "LaunchScreen" in info_plist and "LaunchScreen.storyboard" in project_yml)
    check("README markdown excluded from app resources", "Models/README.md" in project_yml)
    check("XR layout constants not in real UIKit source", "JarvisXRLayoutModel" not in swift_root + swift_state and "designHeight: CGFloat = 896" not in swift_state)
    check("No fake object model claims", "Object model not installed" in swift_vision and "object_model_required" in swift_router and "Object detection ready" not in swift_router)
    check("Product Swift does not expose Blocked label", '"Blocked"' not in swift_root + swift_state + swift_router)
    check("Product Swift does not keep blocked state case", "case blocked" not in swift_root + swift_state + swift_planner)
    check("Root refused responses stay ready", "setInterfaceState(.ready, hint: response.displayResponse)" in swift_root)

    model.open_help()
    help_text = "\n".join(model.product_surface_texts()).lower()
    check("help opens", model.help_visible)
    check("help explains in-app voice limit", "background wake word is not available" in help_text)
    check("help includes vision commands", "scan this" in help_text and "detect objects" in help_text)
    check("iOS help includes scan read detect", "scan this" in swift_help and "read this" in swift_help and "detect objects" in swift_help)
    check("iOS help avoids data/report wording", "JSON" not in swift_help and "debug" not in swift_help and "approval gate" not in swift_help and "test " not in swift_help.lower())
    model.close_help()

    check("orb tap enters ready", model.orb_tap() == "JARVIS ready")
    check("ready tap starts listening", model.orb_tap() == "Listening")

    model.simulate_partial("scan this")
    check("partial transcript captured", model.partial_transcript == "scan this")
    response = model.endpoint()
    check("silence endpoint routes inspection", response.action == "inspect")
    check("state after voice scan is inspection", model.state == "Inspection")

    model.speaking()
    check("speaking state can be entered", model.state == "Speaking")
    check("speaking tap stops speaking", model.orb_tap() == "JARVIS ready")

    model.toggle_keyboard()
    layout_open = model.layout()
    check("keyboard visible", model.keyboard_visible)
    check(
        "input remains above keyboard",
        layout_open.input_top + preview.INPUT_HEIGHT < preview.PHONE_HEIGHT - preview.SAFE_BOTTOM - preview.KEYBOARD_HEIGHT,
    )
    check("help bounds remain visible in keyboard mode", layout_open.help_bounds[1] >= preview.SAFE_TOP)
    check("compact mode preserves orb", layout_open.orb_size > 120)

    model.toggle_keyboard()
    layout_closed = model.layout()
    check("keyboard hidden", not model.keyboard_visible)
    check("closed layout leaves home indicator", layout_closed.input_top + preview.INPUT_HEIGHT <= preview.PHONE_HEIGHT - preview.SAFE_BOTTOM)

    read_response = model.process("read this")
    check("read this maps to OCR", read_response.action == "ocr")

    detect_response = model.process("detect objects")
    check("detect objects routes inspection", detect_response.state == "Inspection")
    check("detect objects reports model missing", "model" in detect_response.display.lower())

    check("go home routes to Control Mesh", model.process("go home").action == "control_mesh")
    check("tap routes to Voice Control grid", "show grid" in model.process("tap that").display.lower())
    check("router has Control Mesh route for screenshot", "take screenshot" in swift_router and "Take Screenshot" in swift_mesh)

    for command in ["scan this", "read this", "detect objects"]:
        response = model.process(command)
        check(f"priority command remains available: {command}", response.status == "ok")

    for command in ["scan this", "read this", "detect objects", "help", "settings", "diagnostics", "control mesh", "tap that", "scroll down", "go home"]:
        normal = preview.InteractionModel()
        response = normal.process(command)
        surface = "\n".join(normal.product_surface_texts()).lower()
        check(f"normal command does not say blocked: {command}", "blocked" not in surface and "blocked" not in response.display.lower())

    if failures:
        print("JARVIS interaction test failed:")
        for failure in failures:
            print(f"- {failure}")
        write_report(passed, failures)
        return 1

    print("JARVIS interaction test passed:")
    for item in passed:
        print(f"- {item}")
    write_report(passed, failures)
    return 0


def write_report(passed: list[str], failures: list[str]) -> None:
    BUNDLE.mkdir(parents=True, exist_ok=True)
    lines = [
        "JARVIS local interaction report",
        f"timestamp: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"passed: {len(passed)}",
        f"failed: {len(failures)}",
        "",
        "Passed checks:",
    ]
    lines.extend(f"- {item}" for item in passed)
    if failures:
        lines.extend(["", "Failed checks:"])
        lines.extend(f"- {item}" for item in failures)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
