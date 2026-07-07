# JarvisOS Final XR Appliance Kit

JarvisOS is an offline-first transformation project for making the available iPhone XR become Jarvis as much as stock iOS allows. The active v0.7 target is the user's only hardware: iPhone XR on iOS 18.7.9 with no SIM card.

v0.7 freezes feature-building and turns the repo into the Final XR Appliance Deployment Kit. The recommendation is: do not jailbreak this XR right now. Use Managed Jarvis Appliance Mode, with supervised Single App Mode if a Mac and Apple Configurator are available, and Guided Access as the immediate fallback.

## What exists now

- 400 structured capabilities in `core/registry/capabilities.json`
- Registry validation in `core/registry/validate_registry.py`
- Offline-first command routing prototype in `core/router`
- 25 plus prototype execution handlers in `core/router/handlers.py`
- SQLite local memory in `core/router/local_memory.py`
- Stateful mock phone profiles in `core/router/phone_state.py`
- One-shot and interactive CLI demo in `mock/cli_demo/jarvis_cli.py`
- Daemon-ready service harness in `core/daemon`
- Hardware and model adapter interfaces in `core/adapters`
- iPhone XR active device profile in `core/device_profiles`
- Ownership mode model in `core/ownership`
- Device takeover feasibility gate in `core/ownership/takeover_gate.py`
- Final XR appliance deployment data in `core/ownership/final_deployment.py`
- XR capability matrix in `core/registry/xr_capability_matrix.json`
- Native shell, daemon, and SpringBoard tweak skeleton documentation
- Shell, daemon, and tweak integration contracts
- Build, risk, test, model, voice, dock, and jailbreak plans

## What this is not

- Not a web app
- Not a chatbot
- Not a cloud AI wrapper
- Not a firmware replacement
- Not a claim that iOS hooks work before jailbroken-device tests
- Not a claim that iPhone XR iOS 18.7.9 jailbreak ownership works
- Not a pass to grow Spotify, browser, or generic app-control features
- Not a request for more conceptual feature-building before physical setup

## Quick verification

```powershell
cd jarvis-iphone6
python core/registry/validate_registry.py
python core/registry/xr_capability_matrix.py
python tests/run_all_tests.py
python core/daemon/jarvis_service.py
'{"type":"health_check","request_id":"h1"}' | python core/daemon/jarvis_service.py --stdio
python mock/cli_demo/jarvis_cli.py "scan this"
python mock/cli_demo/jarvis_cli.py "show phone diagnostics"
python mock/cli_demo/jarvis_cli.py "sync logs to raspberry pi" --dock
python mock/cli_demo/jarvis_cli.py "search current weather online"
python mock/cli_demo/jarvis_cli.py "clear test data with confirmation"
python mock/cli_demo/jarvis_cli.py "clear test data with confirmation" --confirm
python mock/cli_demo/jarvis_cli.py --interactive
```

## Mock Profiles

```powershell
python mock/cli_demo/jarvis_cli.py "scan this" --profile camera_unavailable
python mock/cli_demo/jarvis_cli.py "check sensors" --profile sensors_unavailable
python mock/cli_demo/jarvis_cli.py "show phone diagnostics" --profile low_battery
python mock/cli_demo/jarvis_cli.py --state --profile dock
```

Available profiles include `offline`, `online`, `dock`, `low_battery`, `storage_full`, `camera_unavailable`, `microphone_unavailable`, `gps_unavailable`, `sensors_unavailable`, `private`, and `jailbreak_active`.

## Active Device Boundary

Windows can validate the registry, run the router, execute prototype handlers, use local SQLite memory, run mock state, generate the XR capability matrix, and prepare native contracts. Native XR app deployment, supervised Single App Mode setup, real camera, mic, GPS, sensors, Core ML, Spotify integration, and browser/search behavior require actual device and build-path testing.

Jarvis Core v0.5 pivots the product strategy to iPhone XR Jarvis Device Mode. The native files remain skeletons and have not been compiled or deployed. SpringBoard hooks, launchd daemon installation, root access, lock screen hooks, and system-wide button remaps are blocked until a verified jailbreak lane exists for this device.

Jarvis Core v0.6 adds the takeover feasibility gate. Current XR cannot meet true JarvisOS ownership without a verified jailbreak. The best non-jailbreak approximation is managed appliance mode or supervised kiosk mode.

Jarvis Core v0.7 freezes the project for physical setup. The next step is to use `docs/XR_SETUP_NOW.md` and `docs/XR_PHYSICAL_SETUP_CHECKLIST.md` on the XR, then report what happened.
