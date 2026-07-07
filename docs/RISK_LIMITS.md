# Risk Limits

## Possible

- Final XR appliance setup planning.
- Device takeover feasibility classification.
- Managed appliance planning.
- iPhone XR native Jarvis Device Mode as the active product path.
- Supervised Single App Mode planning as the strongest non-jailbreak ownership route.
- Guided Access fallback planning.
- Offline command routing.
- Smarter local fuzzy routing with mode, hardware, and risk gates.
- Prototype handler execution for a limited subset of capabilities.
- SQLite local memory in the Windows development harness.
- Daemon-style JSON request and response harness on Windows.
- Objective-C model and UIKit shell skeleton generation.
- Adapter-backed mock hardware and model architecture.
- Device profile and ownership mode strategy.
- XR capability matrix classification.
- Native shell UI.
- Local memory and logs.
- Camera capture, QR scanning, basic image utilities.
- Timers, notes, diagnostics, and sensor displays.
- Dock sync with Raspberry Pi or Windows PC.
- Jailbreak daemon and selected hooks if the device and iOS version support them.

## Uncertain

- Whether the physical XR setup succeeds as intended.
- Whether Mac/Xcode or Apple Configurator are available.
- Whether the user has supervision tooling for managed appliance mode.
- Whether the user should wait, change hardware/iOS target, or build the appliance approximation now.
- Actual supervised Single App Mode setup until the user confirms Mac, Apple Configurator, or MDM access.
- Native XR app build path until Swift/UIKit, SwiftUI, or Objective-C/UIKit is chosen.
- Spotify playback control and return-to-Jarvis flow.
- Browser/search behavior inside hard lockdown.
- Stable SpringBoard dominance across all flows.
- Gesture or button remapping.
- Touch ID use beyond exposed APIs.
- Local STT quality.
- Low-FPS live object detection.
- OCR compatibility before the exact iOS version is known.
- Whether the exact handler architecture can be reused unchanged inside a jailbroken daemon.
- Which local daemon transport will be stable under the selected jailbreak.
- Whether generated Objective-C skeletons need significant changes for the final iOS toolchain.
- Whether adapter boundaries need changes for real iOS APIs, jailbreak file access, or dock transports.

## Not Realistic

- Full Apple firmware replacement.
- GPT-level offline reasoning on iPhone 6.
- Large vision-language model running locally.
- Claiming OS hooks work before device tests.
- Claiming XR iOS 18.7.9 jailbreak ownership without verified support and device tests.
- Treating a normal app as the final JarvisOS identity.

## v0.4 Boundary

Jarvis Core v0.4 proves the command, memory, handler, mock-state, daemon request/response, confirmation token, mode transition, adapter, and native skeleton generation harnesses on Windows. It does not prove native iOS behavior, launchd behavior, daemon IPC on device, SpringBoard hooks, camera hardware, microphone hardware, GPS hardware, OCR, YOLO, TTS, STT, or jailbreak package installation.

## Product Boundary

The honest target is a powerful offline action harness with native UI, local tools, small models where practical, local memory, and optional dock or online enhancements.

## v0.5 Boundary

Jarvis Core v0.5 pivots to iPhone XR Device Mode. It does not prove native app deployment, Single App Mode setup, App Store or sideload deployment, real camera, real microphone, real GPS, real sensors, Core ML model execution, Spotify control, browser control, SpringBoard hooks, launchd daemon installation, or root access.

## v0.6 Boundary

Jarvis Core v0.6 is not an app-control pass. It pauses feature growth and classifies feasibility. The current XR cannot meet true JarvisOS ownership now unless a verified jailbreak route appears. Managed appliance mode is the best non-jailbreak approximation.

## v0.7 Boundary

Jarvis Core v0.7 is the final setup kit before touching the XR. It does not create an installable iOS app, does not jailbreak the phone, and does not add app orchestration. It freezes the repo until physical setup is attempted.
