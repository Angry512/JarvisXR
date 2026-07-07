# Offline Voice v0.4

This plan does not claim STT, TTS, or wake word works on the iPhone yet.

## Activation

Push-to-talk first. Foreground wake later. Jailbreak gesture or button activation after the actual jailbreak path is known and tested.

## STT Candidates

- Tiny command grammar recognizer.
- Local short-phrase recognizer if compatible.
- Dock or Pi transcription only as an enhancement.

## TTS Candidates

- Local iOS speech synthesis first.
- Future local voice pack only if storage and CPU budget allow.
- Keep wording formal, concise, and British-style where system voices permit.

## Latency Targets

- Push-to-talk UI response under 150 ms.
- Short command transcript target under 1000 ms if local STT is feasible.
- TTS start target under 500 ms.

## Storage And Memory

- Keep voice assets small.
- Avoid large acoustic models on device.
- Cache only needed prompts and recent responses.

## Mocked Now

- Microphone session.
- STT transcript.
- TTS synthesis.
- Speaker playback.

## Raspberry Pi Testing

- Test heavier STT models.
- Test voice package build and compression.
- Test dock sync of voice resources.

## Requires iPhone Hardware

- Microphone capture quality.
- Speaker output.
- AVAudioSession behavior.
- Battery and thermal behavior.

## Unrealistic

- Cloud voice as core identity.
- Always-on wake word on iPhone 6 without battery proof.
- Large local conversational voice model.
