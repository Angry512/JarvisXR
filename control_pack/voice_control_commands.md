# Voice Control Commands

Use iOS Voice Control for global actions that a normal app cannot perform.

| Phrase | iOS layer | Setup path | Can do | Cannot do | Confirm | Risk |
|---|---|---|---|---|---|---|
| Jarvis open | Voice Control or Shortcut | Accessibility, Voice Control, Custom Commands | Open JARVIS | Force boot ownership | No | low |
| Jarvis inspect | Vocal Shortcut plus Shortcut | Vocal Shortcuts, run JARVIS Inspect | Open JARVIS inspection | Run OCR unless later built | No | low |
| Jarvis quiet | Vocal Shortcut plus URL | Open `jarvis://command?text=quiet%20mode` | Disable speech | Silence system audio globally | No | low |
| Jarvis normal | Vocal Shortcut plus URL | Open `jarvis://command?text=normal%20mode` | Restore JARVIS speech | Change system ownership | No | low |
| Jarvis diagnostics | Vocal Shortcut plus URL | Open `jarvis://diagnostics` | Open diagnostics | Read hidden system logs | No | low |
| Jarvis camera | Voice Control | Voice Control custom command | Open Camera app or JARVIS inspection | Control camera in other apps secretly | No | low |
| Jarvis scroll down | Voice Control | Built-in command | Scroll visible screen | Scroll hidden apps | No | low |
| Jarvis scroll up | Voice Control | Built-in command | Scroll visible screen | Scroll hidden apps | No | low |
| Jarvis tap | Voice Control | Say Show Grid, then Tap number | Tap visible grid point | Inject hidden taps | Sometimes | medium |
| Jarvis show grid | Voice Control | Built-in command | Show numbered grid | Understand app content | No | low |
| Jarvis go home | Voice Control | Built-in command | Return Home if iOS allows | Own SpringBoard | No | medium |
| Jarvis open settings | Voice Control | Built-in command | Open Settings | Change every setting silently | Sometimes | medium |
| Jarvis open camera | Voice Control or Shortcut | Open Camera action if available | Open Camera app | Make JARVIS system camera | No | low |
| Jarvis open Spotify | Voice Control or Shortcut | Open App, Spotify | Open Spotify | Guarantee playback control | No | medium |
| Jarvis open Safari | Voice Control or Shortcut | Open App, Safari | Open Safari | Make Safari part of JARVIS | No | medium |
| Jarvis take screenshot | Voice Control | Built-in if available | Trigger screenshot | Read or edit screenshot automatically | No | medium |
| Jarvis search | Shortcut | Search web or open Safari | Start search flow | Work offline as web search | No | low |
| Jarvis dictate | Voice Control | Built-in dictation | Enter text in focused field | Dictate into locked fields | No | medium |
| Jarvis paste | Voice Control | Built-in paste | Paste clipboard | Bypass app permissions | Sometimes | medium |
| Jarvis return | Shortcut or Voice Control | Open JARVIS app or URL | Return to JARVIS | Force return from every lock state | No | low |

Use Voice Control vocabulary exactly as iOS expects. Test each phrase before enabling Guided Access.
