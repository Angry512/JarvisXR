# Capability To Adapter Map

This map keeps capabilities honest by declaring which adapter families they require.

## Camera Inspection

`camera_inspection` maps to camera, vision, flashlight, and memory adapters. Offline mode should support still-frame scan and save observation. Dock mode may later run heavier analysis.

## OCR And Text

`ocr_text` maps to camera, OCR, TTS, and memory adapters. Offline mode should read still frames when local OCR is available. Dock mode can enhance OCR quality.

## Object Detection

`object_detection` maps to camera, vision, and memory adapters. Offline mode targets small models. Live detection is later.

## Audio And Voice

`audio_voice` maps to microphone, STT, TTS, and speaker adapters. Push-to-talk is first. Wake phrase is later.

## Field Tools

`field_tools` maps to camera, location, sensors, and memory adapters. Offline behavior must save useful observations without network.

## Navigation And Location

`navigation_location` maps to location, compass, and memory adapters. GPS availability and permission state must be visible.

## Sensor Tools

`sensor_tools` maps to sensor adapters. Sensor mode must refuse cleanly when hardware is unavailable.

## Phone Control

`phone_control` maps to future jailbreak or iOS bridge adapters. Do not claim control before device tests.

## Diagnostics

`diagnostics` maps to battery, storage, network, and sensor adapters.

## Dock Families

`raspberry_pi_dock` and `windows_pc_dock` map to dock adapters. They require dock availability and are enhancements.

## Online Enhancement

`online_enhancement` maps to network adapters. Online mode is blocked by private mode unless explicitly overridden.

## Browser And Search

Browser/search maps to network, local memory, and future native search or browser bridge adapters. Online search is available online native when Wi-Fi exists. Offline fallback uses local knowledge and memory. External Safari handoff is blocked in supervised hard lockdown unless an allowed in-app or return-safe flow is proven.

## Spotify And Media

Spotify maps to speaker, network, future App Intent or URL handoff bridge, and possible Spotify SDK investigation. Downloaded Spotify content may work offline inside Spotify, but Jarvis control is uncertain until device testing. External Spotify handoff is available in soft ownership and blocked in hard lockdown unless integrated.

## XR Capability Matrix

`core/registry/xr_capability_matrix.py` generates `core/registry/xr_capability_matrix.json` with these labels:

- `available_offline_native`
- `available_online_native`
- `available_dock`
- `available_soft_ownership`
- `blocked_in_hard_lockdown`
- `blocked_until_jailbreak`
- `uncertain_needs_device_test`

## Modes

Offline capabilities should work without network. Online capabilities require network. Dock capabilities require dock. Hybrid capabilities can begin locally and improve through online or dock paths.
