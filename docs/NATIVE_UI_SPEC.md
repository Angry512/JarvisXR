# Native UI Spec

## Target

- Device: iPhone 6.
- Design size: 375 by 667 points.
- Orientation: portrait-first. Lock portrait until landscape has a tested reason.
- Technology: UIKit with Objective-C or Swift compatible with old iOS constraints.
- Interface rule: no HTML, CSS, React, Tailwind, or embedded web layout as the final shell.

## Visual Direction

Premium, restrained, fast, and functional. The UI should feel like a high-end command instrument: dark graphite base, precise typography, thin status marks, clear mode color, and minimal ornament.

## Core Components

- Central status orb: voice activity, command state, listening state, routing state.
- Mode strip: offline, online, dock, inspection, field, sensor, privacy.
- System row: battery, storage, signal states, daemon state, jailbreak state.
- Command card: transcript, selected capability, confidence, mode, risk, confirmation.
- Action rail: camera, sensors, memory, capabilities, dock, safety.

## Screens

### Jarvis Home

Large central orb, current mode, battery and system state, offline or dock indicator, and quick access to command, camera, sensors, memory, and safety.

### Command Screen

Shows voice or typed transcript, routed capability, confidence, hardware needed, response, alternates, and confirmation controls for risky actions.

### Camera and Inspection

Native camera-first view with scan, OCR, object detection, flashlight, freeze frame, save observation, speak result, and fail states for missing camera permission.

### Sensor Mode

Compass, level, movement, barometer trend, vibration estimate, light, GPS, and diagnostics. Every sensor tile has unavailable, degraded, and active states.

### Capability Browser

Searchable native list grouped by offline, online, dock, hybrid, and system functions. Each row shows mode, hardware, risk, and test status.

### Memory and Logs

Local notes, observations, photos, command history, sensor logs, and export options. Destructive actions require confirmation.

### Dock and Sync

Shows Raspberry Pi or Windows PC availability, last backup, package version, model version, sync status, and errors.

### Safety and Permissions

Shows what Jarvis can control, what requires confirmation, what needs jailbreak, and what is unavailable on the current device.

## Animation and Transitions

Use short native transitions under 250 ms. The orb may pulse during listening and tighten during routing. Avoid heavy blur and expensive effects on iPhone 6.

## Error States

Errors must name the unavailable requirement: no camera permission, no dock, online unavailable, jailbreak required, hardware uncertain, or device test pending.
