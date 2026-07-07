# JARVIS Control Mesh

Control Mesh is the non-jailbreak path for making the iPhone feel as close as possible to a JARVIS device.

JARVIS is the visual brain, voice-first command surface, local memory, speech output, camera inspection surface, and hidden troubleshooting panel. It does not act alone. Official iOS control layers provide the global reach:

- Voice Control handles global navigation, tapping, scrolling, dictation, app opening, Home, and other visible UI actions.
- Vocal Shortcuts provide action phrases such as Jarvis inspect and Jarvis quiet.
- Shortcuts provide allowed multi-step automations.
- URL scheme links send commands into JARVIS with `jarvis://`.
- App Intents are included as source and must be verified by GitHub Actions/Xcode.
- Guided Access can keep JARVIS foreground after testing.
- Switch Control and AssistiveTouch can support repeated gestures when useful.

In the app, phone-level commands return one short next action. Examples: `show grid` returns the exact Voice Control phrase, `open Spotify` attempts the public URL route, `make the screen darker` routes to a dimming Shortcut or Voice Control, and `companion mode` states that arbitrary floating UI is not available through public iOS APIs.

Natural phrases such as `show me how to tap that`, `scroll this page`, `play music`, `go back to Jarvis`, and `take a screenshot` route through the same Control Mesh surface.

This is not true OS takeover. SpringBoard hooks, lock screen hooks, root daemons, hidden screen reading, injected taps, and global button remaps remain jailbreak-only.
