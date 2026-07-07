# Native Bridge

Jarvis Core prepares the future native shell to talk to the Jarvis service contract. In v0.5 the active target is iPhone XR Jarvis Device Mode, while the jailbreak `jarvisd` lane is preserved for future verified support.

## Generated Models

The generator at `native/ios/JarvisShell/scripts/generate_models.py` reads:

- `core/registry/capabilities.json`
- `core/daemon/schemas/*.json`

It writes Objective-C skeleton models to `native/ios/JarvisShell/generated`.

## UIKit Skeleton

`native/ios/JarvisShell/JarvisShellNative` contains Objective-C skeletons for:

- app delegate
- root controller
- home screen
- command screen
- camera inspection
- sensors
- capability browser
- memory
- dock
- settings and safety
- theme
- command client
- local daemon transport
- design tokens

## Boundary

These files are not compiled proof. They define responsibilities, state flow, and future service handoff. Actual XR deployment waits for the native build path, signing path, and device setup. Jailbreak-backed IPC waits for verified XR iOS 18.7.9 support.

## v0.4 Alignment

The native side should expect daemon responses with:

- command status
- mode
- spoken response
- display response
- candidate capabilities
- confirmation token when required
- unavailable reason
- adapter result data when present
- logs written

The native shell should not infer hardware availability locally when daemon state is available. It should render adapter status from response data and use explicit confirmation before sending `confirm_and_execute`.

## v0.5 Alignment

The native side should also expect:

- `get_device_profile`
- `compare_device_profiles`
- `get_device_mode_strategy`
- `get_ownership_modes`
- `set_ownership_mode`
- `get_current_ownership_mode`
- `list_blocked_ownership_features`
- `get_spotify_strategy`
- `list_media_capabilities`

These requests use the same response envelope as command execution. Adapter status, hardware unavailable state, spoken response, display response, mode, confirmation, and logging fields remain stable.
