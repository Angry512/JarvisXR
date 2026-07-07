# Jailbreak Strategy

## Version First

The exact iOS version must be identified before choosing a jailbreak path. iPhone 6 commonly spans older iOS versions, and jailbreak compatibility depends on that version, patch state, and tooling availability.

## What Jailbreak Provides

Jailbreak can provide runtime control, launchd daemons, filesystem access, package installation, SpringBoard tweaks, gesture hooks, and deeper integration than App Store rules allow.

## What Jailbreak Does Not Provide

Jailbreak does not mean Jarvis permanently replaces Apple's full boot chain. iOS still initializes hardware, radios, display, touch, power management, sensors, and many protected services. Jarvis should sit above iOS as the dominant shell where tested access permits.

## Likely Controllable Areas

- Launch Jarvis after jailbreak activation.
- Run a Jarvis daemon through launchd.
- Store local files outside normal app sandbox limits.
- Hook selected SpringBoard behavior if compatible.
- Hide or reduce normal phone clutter if hooks are stable.
- Route button or gesture events if available and tested.

## Uncertain or Limited Areas

- Touch ID integration beyond available APIs.
- Low-level radio control.
- Secure Enclave behavior.
- Full lock screen replacement.
- Boot-time behavior before jailbreak activation.
- Any hook not tested on the actual phone and iOS version.

## Post-Jailbreak Test Sequence

1. Record device model, storage, battery state, and exact iOS version.
2. Confirm jailbreak tool compatibility from current trusted sources.
3. Jailbreak with recovery plan ready.
4. Install a harmless test package.
5. Install launchd daemon skeleton and verify startup logs.
6. Install Jarvis shell and verify foreground stability.
7. Install SpringBoard tweak skeleton with no invasive hooks.
8. Test one hook at a time.
9. Verify safe mode recovery.
10. Document confirmed, failed, and unstable behaviors.
