# XR Hardware Advantage Plan

Target device: iPhone XR on iOS 18.7.9.

This plan audits how JARVIS uses the XR today and where the app is prepared for future local hardware intelligence. It does not claim jailbreak, root access, cloud AI, or untested model behavior.

## Camera Advantage

Active now:

- Rear camera inspection mode through AVFoundation.
- Camera permission request.
- Live preview.
- Photo capture.
- Torch toggle where the active camera supports it.
- Continuous autofocus where supported.
- Continuous auto exposure where supported.
- Captured image size, byte count, and orientation metadata.
- Post-capture Vision text recognition where supported.
- Post-capture barcode and QR detection where supported.

Commands:

- `scan this`
- `take photo`
- `camera status`
- `inspection mode`
- `open camera`

Not active yet:

- Object detection.
- Scene understanding.

Future hooks:

- Route captured images into Core ML analyzers.
- Keep all first-pass model work local.
- Report unavailable models honestly.

## A12 And Core ML Advantage

Prepared now:

- `JarvisVisionInterfaces.swift` defines request, result, capability, and analyzer boundaries.
- The app detects whether a compiled Core ML object detector is bundled.
- `ios/JarvisXR/JarvisXR/Models/` is the model drop-in location.
- `docs/COREML_MODEL_DROPIN.md` defines the accepted compiled model names.

Future local capabilities:

- Image classification.
- Object detection.
- Simple scene labels.

Rules:

- No cloud APIs.
- No paid APIs.
- No claim that a model runs until it is implemented and tested on device.

## Voice Advantage

Active now:

- Local AVSpeechSynthesizer speech output.
- Natural voice profile by default.
- Friendly, Crisp, Quiet, and Formal voice profiles.
- Profile preview in Settings.
- Guarded Personal Voice authorization request on supported iOS versions.
- Speech on, speech off, stop speaking, voice test, and profile commands.
- In-app push-to-talk speech recognition using Speech framework and AVAudioEngine.
- No wake word and no background listening.

## Sensor Advantage

Active or prepared now:

- Battery diagnostics.
- Low Power Mode diagnostics.
- Orientation reporting for the portrait-first app surface where iOS exposes it.
- CoreMotion availability checks for device motion, accelerometer, gyroscope, and magnetometer.
- Field mode command that groups inspection, notes, sensor status, and battery diagnostics.

Commands:

- `sensor status`
- `field mode`
- `motion status`
- `orientation status`
- `compass status`
- `low power status`
- `device status`

Not requested by default:

- Location.
- Compass heading through CoreLocation.

Reason:

Location permission should be requested only when a real location feature is implemented and documented.

## Display And UI Advantage

Active now:

- Portrait-first iPhone interface.
- One strong central orb.
- Full-screen voice-first home surface.
- Dark high-contrast device surface.
- No visible XR branding in product UI.
- No Recent Activity panel on the main screen.
- No large response box on the main screen.

## Security And Appliance Advantage

Active setup path:

- Guided Access after first-run tests.
- Device restrictions and cleaned Home Screen outside the app.
- Control Mesh setup through official iOS layers.

Not claimed:

- Private Face ID access.
- Secure Enclave access.
- Lock screen ownership.
- SpringBoard hooks.

## Connectivity Advantage

Active now:

- Offline-first local commands.
- Wi-Fi optional.
- Control Mesh uses Voice Control, Vocal Shortcuts, Shortcuts, URL scheme, and Guided Access.

Not required:

- Cellular data.
- Cloud AI.

## Diagnostics Matrix

Diagnostics should show:

- Camera: active, available, denied, restricted, or not requested.
- Voice output: active or disabled.
- Voice input: available when iOS grants microphone and Speech recognition permission.
- Motion/sensors: available or unavailable.
- Low Power Mode: enabled or disabled.
- Vision: OCR and barcode available after capture where supported.
- Core ML object detection: model required.
- Control Mesh: active as setup architecture.
- Guided Access readiness: active or ready when enabled.

## Current App Changes

- The main JARVIS surface keeps one central orb and moves utilities into a compact menu so the XR display feels like a dedicated device surface.
- The orb can enter standby from direct interaction or command routing.
- `xr hardware` and `hardware advantage` summarize the active, inactive, and future hardware layers.
- `sensor status`, `orientation status`, `motion status`, `compass status`, `low power status`, and `field mode` route to the same local sensor status surface.
