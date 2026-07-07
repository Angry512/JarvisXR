# Product Design Audit Handoff

Product name:
JARVIS

Target device:
iPhone XR, portrait, native Swift/UIKit. Windows preview uses Python/tkinter as a local approval surface.

Target screens and states:

- Home idle or ready
- Listening
- Heard you
- Processing
- Speaking
- Done
- Keyboard compact mode
- Help sheet
- Mesh sheet
- Inspection
- Permission denied
- Object model missing

Visual direction:
Premium dark command appliance, central glowing cyan orb, sparse controls, high contrast text, calm but powerful motion, no dashboard clutter.

Avoid:

- Terminal UI
- Chatbot layout
- Visible JSON
- Debug labels
- Recent Activity
- Large response panels
- Generic settings-page styling
- Entertainment-first examples

Control philosophy:
JARVIS is the command surface. Mesh routes phone-level actions through official iOS layers: Voice Control, Shortcuts, App Intents, URL schemes, Guided Access, and jarvis:// return links.

Inspection-first philosophy:
The flagship flow is scan, read, look, detect. OCR and barcode scanning use Apple Vision after capture. Object detection is model-gated until a compiled Core ML model is bundled.

Artifacts to inspect:

- `dist/production_visual_review/*.txt`
- `dist/jarvis_local_approval_bundle/latest_visual_report.txt`
- `preview/windows_jarvis_preview/jarvis_preview.py`
- `ios/JarvisXR/JarvisXR/JarvisRootViewController.swift`
- `ios/JarvisXR/JarvisXR/JarvisHelpViewController.swift`

What to critique:

- Does the phone frame feel like JARVIS rather than a test app?
- Is Mesh understandable without explanation from the developer?
- Are Listening and Speaking visually distinct?
- Does keyboard compact mode still feel designed?
- Does Inspection feel like a scan surface rather than a camera utility?
- Are limitations honest without making the product feel weak?
