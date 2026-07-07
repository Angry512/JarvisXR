# Spotify Strategy

Spotify is already installed on the iPhone XR. Jarvis should make Spotify feel controlled by Jarvis, not like the user is merely switching apps.

## Ground Rules

- Offline Spotify only works for content downloaded inside Spotify.
- Online Spotify requires Wi-Fi for search, streaming, and most remote content.
- The repo does not claim Spotify playback control until tested.

## Control Options

1. Open Spotify content links from Jarvis.
2. Investigate Spotify iOS SDK or App Remote.
3. Investigate Shortcuts or Siri bridge if useful.
4. Use external app handoff with return-to-Jarvis strategy in Soft Ownership Mode.

## Ownership Modes

Hard Ownership Mode:

- Jarvis remains foreground.
- External Spotify use is limited or unavailable unless an approved integration works.
- Supervised Single App Mode may block external app handoff.

Soft Ownership Mode:

- Jarvis can open Spotify and guide return.
- This feels less owned, but may be practical before hard integration exists.

## Service Surface

Jarvis Core v0.5 exposes:

- `get_spotify_strategy`
- `list_media_capabilities`

These report strategy and mode-dependent availability only. They do not claim playback control.
