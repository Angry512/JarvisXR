# Product Spec

## Vision

JarvisOS turns an old iPhone 6 into a dedicated Jarvis device. The main product is the phone, not a companion server, browser app, chatbot page, or cloud service. The user should pick up the iPhone 6 and feel that Jarvis is the device.

The device is offline-first. With no cellular data and no Wi-Fi, Jarvis should still route commands, inspect camera input where native implementation allows, read and store local notes, operate timers, report diagnostics, use sensors, keep logs, and expose a searchable list of offline tools.

## Product Identity

Jarvis keeps iOS as the hardware driver layer. It does not promise a full Apple firmware replacement. The project goal is to place a native Jarvis shell, a jailbreak daemon, and tested SpringBoard hooks above iOS so Jarvis dominates the user-facing experience as much as technically possible.

## Core Requirements

- Native iPhone 6 UI, not HTML or CSS.
- Portrait-first 375 by 667 point design target.
- Offline command routing as the default identity.
- Capability registry with explicit modes: offline, online, dock, hybrid.
- No paid APIs.
- No cloud AI dependency for core operation.
- Jailbreak later, after the exact iOS version is known.
- No claims about hooks, daemons, or shell dominance until a jailbroken-device test proves them.

## Role of Raspberry Pi and Windows PC

The Raspberry Pi and Windows PC are dock tools. They can sync logs, back up state, package builds, update models, and run heavier processing, but they are not the product. Jarvis must still have useful offline behavior on the iPhone 6 without them.

## First-Pass Goal

This pass creates a testable repository foundation: architecture docs, native and jailbreak skeletons, capability registry, router prototype, mock phone state, CLI demo, and validation tests.
