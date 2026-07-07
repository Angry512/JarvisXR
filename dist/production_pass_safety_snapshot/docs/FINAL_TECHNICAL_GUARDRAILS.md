# Final Technical Guardrails

- JARVIS uses public iOS APIs only.
- Speech input is in-app and user-started.
- Speech output uses AVSpeechSynthesizer.
- Vision uses Apple Vision framework after capture.
- Core ML object detection is model-gated. A compiled model must be bundled before object detection is claimed.
- Phone-level control routes through App Intents, Shortcuts, Voice Control, URL schemes, or user-guided Control Mesh.
- Guided Access is the non-jailbreak appliance layer.
- No private APIs.
- No jailbreak claims.
- No background wake word.
- No hidden global taps.
- No hidden screen reading.
- No arbitrary floating overlay.
- No root daemon.
