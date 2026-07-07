# Offline Intelligence

Jarvis is tool-first. Commands are classified into registered capabilities, then routed to local tools, sensor readers, local memory, native UI actions, model adapters, or clean refusals.

## First-Pass Implementation

- Typed command routing in Python.
- Registry-backed capability lookup.
- Offline, online, dock, and hybrid availability gates.
- Mock phone state for camera, microphone, sensors, battery, storage, and network.
- Tests for routing and registry validity.

## Later Device Implementation

- Native shell sends commands to local router.
- Daemon keeps registry and memory indexes warm.
- Speech recognition feeds transcripts into the same router.
- Camera and sensor modes execute native tools.
- Jailbreak hooks trigger shell actions only after device proof.

## Non-Goal

GPT-level offline reasoning is not a realistic iPhone 6 target. The realistic target is a powerful local action harness with small models, deterministic tools, local memory, and optional dock intelligence.
