from __future__ import annotations

import json
import subprocess
import sys


PREFERRED_NAMES = [
    "iPhone XR",
    "iPhone 11",
    "iPhone 11 Pro Max",
    "iPhone 14 Plus",
    "iPhone 15 Plus",
    "iPhone 16 Plus",
]


def main() -> int:
    try:
        raw = subprocess.check_output(
            ["xcrun", "simctl", "list", "devices", "available", "-j"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
        data = json.loads(raw)
    except Exception:
        return 1

    devices = [
        device
        for runtime_devices in data.get("devices", {}).values()
        for device in runtime_devices
        if device.get("isAvailable") and "iPhone" in device.get("name", "")
    ]
    for preferred in PREFERRED_NAMES:
        for device in devices:
            if device.get("name") == preferred:
                print(device.get("udid", ""))
                return 0
    if devices:
        print(devices[0].get("udid", ""))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
