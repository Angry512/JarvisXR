# Voice Stack Plan

## Activation Path

Push-to-talk is the reliable first mode. Foreground wake phrase is later. Jailbreak gesture or button activation is later and must be tested on device.

## Speech Recognition

Local STT candidates must be small enough for iPhone 6 or routed through dock mode. The first prototype accepts typed commands. A later native build can use short-phrase recognition where feasible.

## Text to Speech

Use local iOS speech synthesis if available and stable. The voice should be formal, concise, and British-style where system voices permit. No paid or cloud TTS is required for core identity.

## Siri Boundary

Siri Shortcuts may be a temporary convenience bridge. Siri is not the core wake system and not the core identity.

## Failure Behavior

If speech recognition is uncertain, Jarvis displays the transcript, confidence, chosen capability, and a manual correction path.
