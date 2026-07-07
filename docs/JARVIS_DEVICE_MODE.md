# Jarvis Device Mode

v0.7 freezes Jarvis Device Mode into a practical XR setup path. The chosen current path is Managed Jarvis Appliance Mode. The user should now attempt physical setup rather than request more conceptual feature-building.

Jarvis Device Mode now means a device takeover strategy, not app orchestration. Jarvis is meant to be the phone. A normal app, even a polished native app, is not the final identity.

## v0.6 Ownership Modes

- `normal_app_mode`: rejected as final identity.
- `native_shell_mode`: useful foundation, still an app, rejected as final identity.
- `restricted_device_mode`: strip the phone down and reduce escape paths, but iOS still owns the system.
- `supervised_kiosk_mode`: strongest hard lock without jailbreak when Single App Mode or Guided Access is available.
- `managed_appliance_mode`: best current non-jailbreak target using supervision, restrictions, app allow lists, and recovery planning.
- `jailbroken_jarvisos_mode_blocked`: true goal, blocked until a verified XR iOS 18.7.9 jailbreak exists.
- `firmware_replacement_mode_impractical`: effectively not practical because of Apple secure boot and signing.

## What Moves To The Background

Spotify, web search, browser flows, Shortcuts, App Intents, and app handoff are secondary utilities. They can exist only when they reinforce Jarvis as the device identity. They are not the product center.

## Best Current Non-Jailbreak Path

Managed Jarvis Appliance Mode:

- no SIM
- remove unnecessary apps
- configure Focus
- configure Screen Time
- restrict app access
- use supervised Single App Mode if available
- use Guided Access as fallback
- make the native Jarvis shell the visible appliance surface
- keep offline voice, camera, sensors, memory, and utilities central

Use `XR_SETUP_NOW.md` and `XR_PHYSICAL_SETUP_CHECKLIST.md` for the physical setup attempt.

## True Ownership Boundary

SpringBoard hooks, lock screen hooks, launchd daemon install, root access, global button remaps, arbitrary screen reading, arbitrary typing, and system-wide app inspection remain blocked until a real system-level route exists and is tested.
