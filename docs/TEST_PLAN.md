# Test Plan

## v0.7 Final XR Appliance Tests

- Verify final recommendation says do not jailbreak this XR right now.
- Verify final recommendation chooses appliance mode.
- Verify XR setup steps are non-empty.
- Verify no-jailbreak warning includes A12, iOS 18.7.9, and unverified tool warning.
- Verify appliance mode plan exists.
- Verify native build decision tree includes Mac/Xcode, Apple Configurator, and Windows-only paths.
- Verify release freeze, final handoff, physical setup checklist, and identity spec exist.
- Run all previous tests.

## v0.6 Device Takeover Gate Tests

- Verify takeover levels exist.
- Verify firmware replacement is impractical.
- Verify normal app mode is rejected as final identity.
- Verify supervised kiosk is buildable when setup exists.
- Verify jailbroken JarvisOS is the true goal but blocked.
- Verify SpringBoard, lock screen, and button remap requirements are jailbreak only.
- Verify camera, mic, and sensors are native app possible.
- Verify appliance mode steps exist.
- Verify app orchestration is secondary.
- Verify Spotify and search are optional modules.
- Verify daemon requests expose takeover levels, true ownership requirements, recommended path, blockers, jailbreak-only features, supervision features, and appliance steps.

## v0.5 XR Device Mode Tests

- Validate active profile is iPhone XR on iOS 18.7.9.
- Validate iPhone XR profile fields.
- Verify daemon service requests for device profile, profile comparison, and Device Mode strategy.
- Verify ownership mode listing, set, get, blocked feature reporting, and jailbreak-blocked refusal.
- Verify Spotify strategy and media capability service responses.
- Generate and validate XR capability matrix.
- Verify camera, OCR, and vision are classified native possible.
- Verify online search remains online native and blocked in hard lockdown.
- Verify Spotify is mode-dependent or needs device testing.
- Verify SpringBoard, launchd, root, and button remap surfaces remain blocked until jailbreak.
- Verify dock functions stay dock only.
- Run all existing v0.4 adapter, router, daemon, confirmation, and mock hardware tests.

## Phase 1: Windows Repository Tests

Validate file structure, Python imports, registry shape, router behavior, local memory, handler output, mock phone state, and CLI examples.

## Phase 2: Capability Registry Validation

Run `python core/registry/validate_registry.py` and confirm at least 400 valid capabilities.

## Phase 3: Command Router Tests

Run `python -m pytest core/router/tests`.

Jarvis Core v0.2 router tests include:

- fuzzy routing
- related-tool queries
- unavailable hardware refusals
- online-only refusal in offline mode
- dock-only refusal when not docked
- high-risk confirmation behavior
- handler output format
- low-confidence candidate output
- CLI rendering helpers

## Phase 3A: Daemon Service Tests

Run `python -m pytest core/daemon/tests`.

v0.3 daemon tests include request validation, response validation, health checks, command routing, command execution, capability listing, mock state updates, hardware refusals, online refusals, dock refusals, privacy blocking, confirmation tokens, stale token refusal, mode transitions, memory operations, generated native model existence, and handler output shape.

## Phase 3B: Adapter Tests

Run `python -m pytest core/adapters/tests`.

v0.4 adapter tests include mock result shape, adapter registry initialization, unavailable camera, unavailable microphone, private network refusal, latency reporting, and dock adapter behavior.

## Phase 4: Mock Hardware Tests

Verify camera, microphone, sensors, GPS, battery, storage, network, private mode, jailbreak state, and dock mock states.

v0.2 mock profiles:

- `offline`
- `online`
- `dock`
- `low_battery`
- `storage_full`
- `camera_unavailable`
- `microphone_unavailable`
- `gps_unavailable`
- `sensors_unavailable`
- `private`
- `jailbreak_active`

## Phase 5: Local Memory Tests

Verify note save, observation save, command history save, search, summary export, and clear-test-data confirmation.

## Phase 6: Native UI Design Review

Review the UIKit screen plan against 375 by 667 point constraints before implementation.

## Phase 7: Jailbreak Readiness Review

Identify exact iOS version, jailbreak tool, recovery process, and package workflow.

## Phase 8: Post-Jailbreak Install Test

Install harmless package, then Jarvis shell skeleton, daemon skeleton, and tweak skeleton.

## Phase 9: Daemon Test

Verify launchd startup, logs, restart behavior, permissions, and failure recovery.

## Phase 10: SpringBoard Tweak Test

Test one hook at a time. Record confirmed, failed, unstable, and recovery behavior.

## Phase 11: Offline Field Test

Disable Wi-Fi and cellular. Test camera, OCR path, QR scan, notes, sensors, timers, diagnostics, and local memory.

## Phase 12: Dock Sync Test

Test Raspberry Pi and Windows PC backup, log sync, package transfer, and model update.

## Phase 13: Performance and Battery

Measure launch time, routing latency, camera latency, model latency, heat, and battery drain.

## Phase 14: Failure Recovery

Confirm safe mode, package removal, daemon stop, and shell fallback.

## v0.2 Windows Verification Commands

```powershell
python core/registry/validate_registry.py
python native/ios/JarvisShell/scripts/generate_models.py
python tests/run_all_tests.py
python core/daemon/jarvis_service.py
python mock/cli_demo/jarvis_cli.py "scan this"
python mock/cli_demo/jarvis_cli.py "show tools related to camera"
python mock/cli_demo/jarvis_cli.py "search current weather online"
python mock/cli_demo/jarvis_cli.py "sync logs to raspberry pi" --dock
python mock/cli_demo/jarvis_cli.py "clear test data with confirmation"
python mock/cli_demo/jarvis_cli.py "clear test data with confirmation" --confirm
```
