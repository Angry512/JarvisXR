# Changelog

## v0.7

- Added Final XR Appliance Deployment Kit.
- Added release freeze document.
- Added final handoff, immediate XR setup guide, physical setup checklist, no-jailbreak warning, appliance build plan, native build decision, and Jarvis identity spec.
- Added final daemon requests for recommendation, setup steps, no-jailbreak warning, appliance mode plan, and native build decision tree.
- Froze feature-building until physical XR setup is attempted.
- Reconfirmed the recommendation: do not jailbreak this XR right now.

## v0.6

- Added Device Takeover Feasibility Gate to stop app-control drift.
- Added takeover hierarchy from normal app through firmware replacement.
- Marked normal app and native shell as rejected final identities.
- Marked managed Jarvis appliance as the best current non-jailbreak approximation.
- Preserved jailbroken JarvisOS as the true goal while marking XR iOS 18.7.9 blocked without verified jailbreak support.
- Added true ownership requirements and appliance mode plan.
- Added XR jailbreak reality check with trusted-source criteria.
- Replaced ownership modes with takeover-focused modes.
- Added daemon requests for takeover levels, requirements, recommendations, blockers, jailbreak-only features, supervision features, and appliance steps.

## v0.5

- Pivoted active target from iPhone 6 jailbreak-first to iPhone XR on iOS 18.7.9.
- Added Jarvis Device Mode strategy with supervised Single App Mode as the preferred non-jailbreak ownership path.
- Added iPhone XR and preserved iPhone 6 device profiles under `core/device_profiles`.
- Added ownership mode model under `core/ownership`.
- Added daemon requests for device profile, device mode strategy, ownership modes, Spotify strategy, and media capabilities.
- Added generated XR capability matrix and tests for native, online, dock, soft ownership, hard lockdown, jailbreak-blocked, and uncertain classifications.
- Added Device Mode, supervised lockdown, browser/search, Spotify, and XR pivot docs.
- Added XR native implementation plan and XR-specific offline vision and voice plans.

## v0.4

- Added hardware and model adapter interfaces under `core/adapters`.
- Added mock adapters for camera, microphone, speaker, TTS, STT, vision, OCR, sensors, location, flashlight, storage, battery, network, and dock.
- Added adapter registry for Windows mocks and future native or dock bridges.
- Connected selected handlers to adapters for scan, OCR, object detection, push to talk, readback, sensors, battery, storage, network, privacy, field mode, and dock sync.
- Added richer native UIKit shell architecture skeletons for app state, modes, command sessions, rendering, status, lists, confirmation, sensors, memory, camera overlay, offline, and dock views.
- Added native flow notes for core Jarvis shell journeys.
- Added offline vision and voice v0.4 plans.
- Added adapter architecture and capability-to-adapter mapping docs.
- Expanded automated tests to 79 total tests.

## v0.3

- Added daemon-ready service layer in `core/daemon`.
- Added stable request, response, capability result, phone state, and confirmation JSON schemas.
- Added JSON-over-stdio service harness for Windows testing.
- Added confirmation token creation, expiration, refusal, and confirm-and-execute flow.
- Added mode transition engine for offline, online, dock, inspection, field, sensor, quiet, privacy, diagnostics, and recovery.
- Tightened handler output shape with side effects, memory writes, logs, and confirmation token fields.
- Added Objective-C native model generator from registry and daemon schemas.
- Added generated Objective-C model skeletons for capabilities, requests, responses, phone state, modes, and confirmations.
- Added native UIKit shell skeleton files and design tokens.
- Added daemon and native bridge docs.
- Expanded automated tests to 48 total tests.

## v0.2

- Added smarter command routing with phrase normalization, fuzzy matching, family-aware scoring, mode hints, hardware refusals, risk confirmations, related-tool queries, and low-confidence candidates.
- Added `core/router/handlers.py` with 25 plus prototype handlers across camera, OCR, object detection, audio, sensors, diagnostics, utilities, memory, and Jarvis modes.
- Added SQLite local memory in `core/router/local_memory.py`.
- Added mutable mock phone state profiles in `core/router/phone_state.py`.
- Upgraded CLI with one-shot mode, interactive sessions, mock profile changes, state flags, command history, note/search paths, and spoken response rendering.
- Added native shell implementation plan v0.2.
- Added shell, daemon, capability, tweak event, permission, confirmation, and safety logging contracts.
- Expanded tests for v0.2 router, memory, handler, refusal, confirmation, and CLI helper behavior.

## v0.1

- Created initial repository structure.
- Added 400-capability registry.
- Added schema validation.
- Added basic command router.
- Added mock phone state modules.
- Added CLI demo.
- Added native iOS, daemon, SpringBoard tweak, dock, model, voice, build, test, and risk planning docs.
