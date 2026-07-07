# Final Product Audit

## What Felt Weak

- The top-left ellipsis did not explain its purpose.
- The preview looked useful, but still leaned toward a review harness rather than a premium phone surface.
- Command routing worked, but the architecture still read as direct string routing instead of a command planner.
- Control Mesh needed to feel more like JARVIS giving an immediate route through official iOS layers.
- Inspection copy needed sharper states and model-gated object detection language.

## What Must Change

- Rename the vague top-left control to Mesh and make its purpose clear.
- Keep the `?` help control and make help a real operating manual.
- Add a deterministic command plan layer behind the existing router.
- Make scan, read, detect, and look commands the primary product routes.
- Keep phone-control responses short, confident, and routed through Voice Control, Shortcuts, URL routes, or Control Mesh.
- Keep the Windows preview as a product surface plus external controls.

## What Must Not Change

- Do not bring back Recent Activity, large response panels, debug chips, or product-facing report output.
- Do not break orb flow: Standby, JARVIS ready, Listening, Inspection, Speaking, Done.
- Keep the app native Swift/UIKit and the preview Python/tkinter.
- Keep OCR and barcode claims tied to Apple Vision after capture.
- Keep object detection gated by a bundled Core ML model.

## Impossible On Non-Jailbroken iOS

- SpringBoard hooks.
- Lock screen hooks.
- Root or launchd daemon behavior.
- Hidden global screen reading.
- Injected global taps.
- Background wake word.
- Arbitrary floating app UI over other apps.

## Strongest Legal Controller Experience

JARVIS should act as the central command surface, then route phone-level actions through public iOS-safe control layers: App Intents where available, Shortcuts, jarvis:// links, Voice Control phrases, URL schemes, Guided Access, and clear user-guided steps.
