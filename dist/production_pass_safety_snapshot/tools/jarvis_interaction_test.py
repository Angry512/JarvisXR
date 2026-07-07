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
    swift_router = (IOS_ROOT / "JarvisCommandRouter.swift").read_text(encoding="utf-8")
    swift_planner = (IOS_ROOT / "JarvisCommandPlan.swift").read_text(encoding="utf-8")
    swift_mesh = (IOS_ROOT / "JarvisControlMeshPlanner.swift").read_text(encoding="utf-8")

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
    check("speaking tap stops speaking", model.orb_tap() == "Done")

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
