# Release Freeze

## Release

v0.7 Final XR Appliance Deployment Kit

## Target

iPhone XR on iOS 18.7.9.

## Final Current Recommendation

Do not jailbreak this XR right now.

## Best Practical Path

Managed Jarvis Appliance Mode.

## Strongest Path If Mac Exists

Supervised Single App Mode using Apple Configurator or an MDM-style setup path.

## Immediate Fallback

Guided Access.

## Verification State

The v0.7 release must pass:

- `python core/registry/validate_registry.py`
- `python native/ios/JarvisShell/scripts/generate_models.py`
- `python tests/run_all_tests.py`

## Freeze Rule

No more feature-building prompts until physical setup is attempted on the XR. The next useful work is setup evidence from the device.

## Still Impossible Without Jailbreak

- SpringBoard hooks.
- Lock screen hooks.
- launchd daemon install.
- Root access.
- Global button remap.
- Arbitrary app control.
- True OS ownership.
