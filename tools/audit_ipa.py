from __future__ import annotations

import argparse
import plistlib
import sys
import zipfile
from pathlib import PurePosixPath


EXPECTED_BUNDLE_ID = "com.amrik.jarvisxr"
EXPECTED_DISPLAY_NAME = "JARVIS"
REQUIRED_INTENT_STRINGS = [
    "Start JARVIS Inspection",
    "Open JARVIS Control Mesh",
    "Return to JARVIS",
    "Run JARVIS Command",
    "Set JARVIS Quiet Mode",
    "Set JARVIS Normal Mode",
]
FORBIDDEN_STRINGS = [
    "Recent Activity",
    "JARVIS RESPONSE",
    "Next test steps ready",
    "Try: open Spotify",
    "play music",
    "raw JSON",
    "debug label",
    "Wi-Fi path available",
    "offline tools remain",
    "guided ready",
]
REQUIRED_HELP_STRINGS = [
    "Tap once from standby",
    "Tap again to listen",
    "Tap while listening",
    "Long hold",
]
FORBIDDEN_APP_DOC_SUFFIXES = (".md", ".markdown", ".rst")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a JARVIS unsigned IPA on Windows.")
    parser.add_argument("ipa", help="Path to JarvisXR-unsigned.ipa")
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []
    passed: list[str] = []

    try:
        archive = zipfile.ZipFile(args.ipa)
    except Exception as exc:
        print(f"IPA audit failed: could not open zip: {exc}")
        return 1

    with archive:
        names = archive.namelist()
        app_roots = sorted({name.split(".app/", 1)[0] + ".app" for name in names if name.startswith("Payload/") and ".app/" in name})
        if len(app_roots) != 1:
            failures.append(f"Expected one Payload/*.app, found {len(app_roots)}")
            app_root = app_roots[0] if app_roots else ""
        else:
            app_root = app_roots[0]
            passed.append(f"App bundle found: {app_root}")

        info_path = f"{app_root}/Info.plist" if app_root else ""
        info = {}
        if info_path and info_path in names:
            try:
                info = plistlib.loads(archive.read(info_path))
                passed.append("Info.plist exists and parses")
            except Exception as exc:
                failures.append(f"Info.plist could not parse: {exc}")
        else:
            failures.append("Info.plist missing from app bundle")

        if info:
            check_equal(passed, failures, "CFBundleDisplayName", info.get("CFBundleDisplayName"), EXPECTED_DISPLAY_NAME)
            bundle_id = info.get("CFBundleIdentifier", "")
            if bundle_id == EXPECTED_BUNDLE_ID or bundle_id.endswith(".jarvisxr"):
                passed.append(f"Bundle identifier acceptable: {bundle_id}")
            else:
                failures.append(f"Unexpected bundle identifier: {bundle_id}")
            if info.get("MinimumOSVersion"):
                passed.append(f"MinimumOSVersion present: {info.get('MinimumOSVersion')}")
            else:
                failures.append("MinimumOSVersion missing")
            if info.get("UILaunchStoryboardName") == "LaunchScreen":
                passed.append("LaunchScreen configured in Info.plist")
            else:
                failures.append("UILaunchStoryboardName is not LaunchScreen")

        launch_candidates = [name for name in names if name.startswith(app_root + "/") and "LaunchScreen" in name]
        if launch_candidates:
            passed.append("LaunchScreen resource present")
        else:
            failures.append("LaunchScreen resource not found in app bundle")

        bundled_docs = [
            name for name in names
            if name.startswith(app_root + "/")
            and PurePosixPath(name).suffix.lower() in FORBIDDEN_APP_DOC_SUFFIXES
        ]
        if bundled_docs:
            failures.append("Markdown or documentation files were copied into the app bundle: " + ", ".join(bundled_docs[:8]))
        else:
            passed.append("No markdown/docs in app bundle")

        combined = read_text_payload(archive, names, app_root)
        intents_seen = any(text in combined for text in REQUIRED_INTENT_STRINGS)
        if intents_seen:
            for text in REQUIRED_INTENT_STRINGS:
                if text in combined:
                    passed.append(f"Intent string present: {text}")
                else:
                    failures.append(f"Expected App Intent string missing from readable bundle payload: {text}")
        else:
            warnings.append("App Intent strings were not visible in readable payload, metadata may be compiler-packed")

        if ".mlmodelc/" not in "\n".join(names):
            if "Object model not installed" in combined:
                passed.append("No .mlmodelc found and object detection is model-gated")
            else:
                failures.append("No .mlmodelc found but model-gated object wording was not detected")
        else:
            passed.append("Compiled Core ML model resource present")

        for text in FORBIDDEN_STRINGS:
            if text in combined:
                failures.append(f"Forbidden product string found: {text}")
            else:
                passed.append(f"Forbidden product string absent: {text}")

        for text in REQUIRED_HELP_STRINGS:
            if text in combined:
                passed.append(f"Help wording present: {text}")
            else:
                failures.append(f"Required tap/hold help wording missing: {text}")

        if "LaunchScreen.storyboardc/" in "\n".join(names) or any(name.endswith("LaunchScreen.storyboardc") for name in names):
            passed.append("Compiled LaunchScreen storyboard present")
        elif any("LaunchScreen" in name for name in names):
            passed.append("LaunchScreen resource present by name")
        else:
            failures.append("No LaunchScreen resource name found")

        if not has_otool():
            warnings.append("otool unavailable on this machine, framework binary inspection skipped")

    print("JARVIS IPA audit")
    for item in passed:
        print(f"PASS: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    for item in failures:
        print(f"FAIL: {item}")
    return 1 if failures else 0


def check_equal(passed: list[str], failures: list[str], label: str, actual: object, expected: object) -> None:
    if actual == expected:
        passed.append(f"{label} == {expected}")
    else:
        failures.append(f"{label} expected {expected}, got {actual}")


def read_text_payload(archive: zipfile.ZipFile, names: list[str], app_root: str) -> str:
    chunks: list[str] = []
    for name in names:
        if not name.startswith(app_root + "/") or name.endswith("/"):
            continue
        try:
            data = archive.read(name)
        except Exception:
            continue
        if b"\x00" in data[:4096] and not name.endswith((".plist", ".strings", ".json")):
            try:
                chunks.append(data.decode("utf-8", errors="ignore"))
            except Exception:
                pass
            continue
        try:
            chunks.append(data.decode("utf-8", errors="ignore"))
        except Exception:
            continue
    return "\n".join(chunks)


def has_otool() -> bool:
    return sys.platform == "darwin"


if __name__ == "__main__":
    raise SystemExit(main())
