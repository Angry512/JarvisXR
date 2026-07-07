# Capability Registry

The registry lives at `core/registry/capabilities.json` and currently contains 400 capabilities.

Each entry includes:

- `id`
- `family`
- `name`
- `example_voice_phrases`
- `mode`
- `required_hardware`
- `risk_level`
- `permission_required`
- `implementation_notes`
- `test_idea`

## Families

- Camera and Inspection
- OCR and Text
- Object Detection
- QR and Barcode
- Audio and Voice
- Field Tools
- Navigation and Location
- Sensor Tools
- Phone Control
- Files and Memory
- Utilities
- Diagnostics
- Security and Privacy
- Developer Tools
- Offline Knowledge
- Emergency Tools
- Jarvis Modes
- Raspberry Pi Dock
- Windows PC Dock
- Online Enhancement

## Mode Rules

Offline capabilities must be useful without internet. Online capabilities require Wi-Fi. Dock capabilities require Raspberry Pi or Windows PC availability. Hybrid capabilities can begin offline but may improve with dock or online services.

## v0.2 Router Behavior

Jarvis Core v0.2 keeps the registry stable while adding smarter command behavior:

- fuzzy phrase routing
- family-aware routing
- mode preference when commands mention offline, online, dock, Pi, or PC
- hardware refusal from mock phone state
- confirmation requirement for risky capabilities
- related-tool queries such as `show tools related to camera`
- low-confidence top candidate lists
- prototype handler execution for a focused capability subset

## Validation

Run:

```powershell
python core/registry/validate_registry.py
```
