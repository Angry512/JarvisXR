from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_SCREENSHOTS = [
    "01-standby.png",
    "02-ready-after-single-tap.png",
    "03-listening-after-second-tap.png",
    "04-processing-result-after-command.png",
    "05-no-speech-ready.png",
    "06-long-hold-standby.png",
    "07-keyboard-open.png",
    "08-help.png",
    "09-control-mesh.png",
    "10-inspection.png",
    "11-object-model-missing.png",
    "12-settings.png",
    "13-diagnostics.png",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify JARVIS iOS visual proof screenshots.")
    parser.add_argument("directory", help="Directory containing PNG screenshots from XCUITest.")
    args = parser.parse_args()

    root = Path(args.directory)
    failures: list[str] = []
    for filename in REQUIRED_SCREENSHOTS:
        path = root / filename
        if not path.exists():
            failures.append(f"missing: {filename}")
        elif path.stat().st_size <= 0:
            failures.append(f"empty: {filename}")

    if failures:
        print("JARVIS visual proof verification failed")
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(f"JARVIS visual proof verification passed: {len(REQUIRED_SCREENSHOTS)} screenshots")
    for filename in REQUIRED_SCREENSHOTS:
        print(f"PASS: {filename}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
