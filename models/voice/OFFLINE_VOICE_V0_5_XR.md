# Offline Voice v0.5 XR

Voice remains offline-first and tool-first. The XR target offers better headroom than iPhone 6, but no STT or TTS stack is claimed until tested.

## Activation Path

- Push-to-talk first.
- Foreground wake later.
- Jailbreak gesture or button activation later, blocked until verified support.

## STT Candidates

- Native Speech framework investigation for offline availability on the target device.
- Small local recognizer investigation if app size, memory, and latency fit.
- Command grammar fallback for a constrained offline phrase set.

## TTS Candidates

- `AVSpeechSynthesizer` first for native spoken response handoff.
- Local custom voice investigation later if storage, quality, and latency are acceptable.
- Formal British-style Jarvis voice direction without childish sci-fi styling.

## Targets

- Push-to-talk response start: under 1000 ms after transcript is available.
- Spoken response handoff: under 500 ms for short phrases.
- Storage: keep voice assets modest until XR storage is known.

## Can Test Now

- Mock microphone, STT, TTS, and speaker adapters.
- Daemon response spoken/display handoff.
- Privacy mode blocking online enhancement.

## Requires Device

- Microphone permission and capture.
- Offline STT feasibility.
- TTS voice quality.
- Background and foreground activation limits.

## Unrealistic

- Always-on system wake phrase without special permissions or jailbreak proof.
- Cloud voice as the core identity.
