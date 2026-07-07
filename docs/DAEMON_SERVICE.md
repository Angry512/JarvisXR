# Daemon Service

Jarvis Core v0.3 introduces a daemon-ready service layer in `core/daemon`.

## Purpose

The service is the future bridge between the native Jarvis shell, `jarvisd`, and eventually SpringBoard tweak events. It is transport-independent at the contract level.

## Windows Test Transport

The current test transport is JSON over stdin and stdout:

```powershell
'{"type":"health_check","request_id":"h1"}' | python core/daemon/jarvis_service.py --stdio
```

This is not a web server and not a UI.

## Supported Requests

- `health_check`
- `route_command`
- `execute_command`
- `list_capabilities`
- `list_offline_capabilities`
- `list_related_capabilities`
- `get_phone_state`
- `update_mock_phone_state`
- `save_note`
- `search_memory`
- `export_memory_summary`
- `request_confirmation`
- `confirm_and_execute`
- `set_mode`
- `get_mode`
- `get_recent_history`

## Response Contract

Every service response includes request id, status, mode, spoken response, display response, data, risk level, confirmation flag, unavailable reason, candidate capabilities, and written log ids.

## Device Boundary

On the iPhone, the transport may become a Unix domain socket, loopback daemon channel, or another jailbreak-compatible local IPC mechanism. That choice waits for the exact iOS version and jailbreak toolchain.

## v0.4 Adapter Data

Selected commands now return mock adapter result data inside `data.handler_data`. Adapter results include status, data, error, latency, and source. The service can be initialized with mock adapters now, and future native or dock adapters later.
