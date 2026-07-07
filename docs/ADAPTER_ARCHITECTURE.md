# Adapter Architecture

Jarvis Core uses adapters so the daemon and router do not need to know whether a result came from Windows mocks, a future native iOS bridge, a local model, or a Raspberry Pi dock.

## Result Shape

Every adapter returns:

- `status`
- `data`
- `error`
- `latency_ms`
- `source`

## Current Adapters

- camera
- microphone
- speaker
- TTS
- STT
- vision
- OCR
- sensor
- location
- flashlight
- storage
- battery
- network
- dock

## v0.5 XR Direction

The active device profile is now iPhone XR on iOS 18.7.9. That changes the preferred future adapter implementation:

- Native iOS public APIs become the primary path for camera, microphone, speaker, sensors, battery, storage, network, location, and Core ML where allowed.
- Supervised Single App Mode becomes the primary ownership context for hard lockdown.
- Shortcuts, App Intents, URL schemes, and share sheet are bridge adapters, not the core identity.
- Jailbreak-backed adapters remain blocked until verified XR support exists.
- Dock adapters remain Raspberry Pi or Windows PC enhancements.

All current adapter implementations remain mocks. They prove contract shape and routing behavior on Windows, not device hardware behavior.

## Safety

Adapters must report unavailable hardware instead of hiding failure. The daemon response must preserve adapter status in `data` so native UI can render precise refusal states.
