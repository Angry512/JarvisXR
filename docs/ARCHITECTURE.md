# Architecture

## v0.7 Final XR Appliance Deployment Kit

v0.7 freezes feature-building. The user only has the iPhone XR, and the practical path is Managed Jarvis Appliance Mode. Supervised Single App Mode is the strongest path if Mac and Apple Configurator are available. Guided Access is the immediate fallback.

The next step is physical setup on the XR, not more Codex architecture. True ownership remains blocked without a verified jailbreak.

## v0.6 Device Takeover Gate

v0.6 intentionally stops app-control feature growth. The active architecture question is whether the iPhone XR can be made into Jarvis, not whether a native app can control Spotify or browser flows.

The hierarchy is now normal app, native shell, restricted device, supervised kiosk, managed appliance, jailbroken JarvisOS, and firmware replacement. Normal app and native shell are rejected as final identity. Managed appliance is the best current non-jailbreak approximation. Jailbroken JarvisOS is the true goal but blocked until verified XR iOS 18.7.9 support exists.

## v0.5 Active Target

The active target is now iPhone XR on iOS 18.7.9. The project no longer treats iPhone 6 as the main product device. The iPhone 6 jailbreak-first architecture remains preserved for a future lane.

Jarvis Device Mode is now constrained by the v0.6 gate: supervised kiosk or managed appliance for non-jailbreak approximation, jailbreak lane for true ownership, and no drift into generic app orchestration.

## Layer 1: Native Jarvis Shell

The shell is a real iOS interface. For the active XR path, Swift/UIKit or SwiftUI should be evaluated next. The old Objective-C/UIKit skeleton remains useful for future jailbreak work. The shell provides Jarvis home, command routing display, inspection camera, sensor mode, capability browser, memory log, dock sync, safety screens, browser/search module, Spotify module, and ownership mode state.

## Layer 2: Jarvis Daemon

The daemon is planned for jailbroken mode and launchd startup after jailbreak activation. It owns command routing services, logs, local memory, capability registry loading, sensor state aggregation, and offline tool execution. This pass includes only design and launchd skeletons.

For XR Device Mode, the daemon service remains a Windows-testable contract harness. A stock iOS app cannot install a launchd daemon or claim root service behavior.

## Layer 3: SpringBoard Tweak

The tweak is planned to make the phone feel owned by Jarvis. It may auto-launch Jarvis, redirect home behavior, suppress clutter, and expose button or gesture activation. These are planned hooks only until device testing confirms them.

On iPhone XR iOS 18.7.9 this lane is blocked pending verified jailbreak support.

## Layer 4: Offline Intelligence

Offline intelligence is tool-first. It classifies commands into registered capabilities and routes them to native tools, local models, local memory, sensors, or safe refusals. It is not a generic chatbot.

Jarvis Core v0.2 adds family-aware fuzzy matching, mode-aware routing, hardware-aware refusals, risk-aware confirmations, related-tool queries, local memory, and prototype handlers. These are still development-harness behaviors until ported into the native shell and daemon.

## Layer 5: Capability Registry

The registry is the contract between voice phrases, UI actions, available modes, required hardware, risk, permissions, implementation notes, and tests. It prevents fake capabilities by forcing every action to declare what it needs.

## Layer 6: Dock Mode

Dock mode activates when a Raspberry Pi or Windows PC is available. It supports backup, package transfer, model update, diagnostics export, and heavier jobs. Dock mode augments Jarvis but does not define Jarvis.

## Layer 7: Model Layer

Small local models are planned for OCR, object detection, wake word experiments, and local command recognition. Large GPT-level offline reasoning is not a realistic iPhone 6 target.

## Layer 8: Sensor Layer

The sensor layer abstracts camera, microphone, speaker, flashlight, GPS, compass, gyroscope, accelerometer, barometer, proximity, ambient light, battery, storage, Wi-Fi, and Bluetooth state where available.

## Layer 9: Safety and Permissions

Risky actions require confirmation. Jailbreak-only actions must remain unavailable until jailbreak state and hook tests are verified. Online and dock actions are gated by availability.

## v0.2 Execution Layer

The Python handler layer maps selected capability IDs to prototype functions. It intentionally covers a focused set of camera, OCR, object, audio, sensor, diagnostics, utility, memory, and Jarvis mode capabilities. The remaining registry entries stay routable but return a structured no-handler response.

## v0.3 Daemon Service Layer

Jarvis Core v0.3 adds a daemon-ready service boundary in `core/daemon`. The service accepts transport-independent JSON requests and returns stable JSON responses for health checks, command routing, command execution, capability listing, phone state, mock state updates, local memory, confirmation tokens, mode transitions, and recent history.

The Windows transport is JSON over stdin and stdout. That transport exists only for testing. On the jailbroken phone, the same request and response contracts can be carried by a local daemon channel after the iOS version and jailbreak route are known.

## v0.3 Native Bridge

The native bridge is represented by Objective-C model skeletons generated from the registry and daemon schemas, plus a UIKit shell skeleton. These files are preparation for future iPhone work. They are not compiled proof and do not claim iPhone control.

## v0.4 Adapter Layer

Jarvis Core v0.4 adds adapter interfaces between handlers and hardware or model capabilities. The daemon and router can call camera, microphone, speaker, TTS, STT, vision, OCR, sensor, location, flashlight, storage, battery, network, and dock adapters without knowing whether the implementation is a Windows mock, future native iOS bridge, or future Raspberry Pi dock bridge.

The current adapters are mocks. They provide real contracts and testable responses, but they do not prove iPhone hardware access.

## v0.4 Native Shell Architecture

The Objective-C UIKit skeleton now includes app state, mode control, command session, response rendering, voice orb, status header, capability list, confirmation view, sensor tile, memory cell, camera overlay, offline banner, and dock status view. These are native structures, not browser UI.

## v0.5 Device Profile And Ownership Layer

Jarvis Core v0.5 adds `core/device_profiles` and `core/ownership`. The active profile is iPhone XR. Ownership modes distinguish native app mode, Guided Access, supervised Single App Mode, soft ownership, and blocked jailbreak ownership. These are strategy and service contracts, not proof of device lockdown.

## v0.6 Takeover Layer

Jarvis Core v0.6 adds `core/ownership/takeover_gate.py`. The daemon can now explain takeover levels, true ownership requirements, the recommended path, why a normal app is rejected, what blocks true ownership, what is jailbreak-only, what supervision can provide, and the steps for appliance mode.
