# Device Takeover Feasibility Gate

JarvisOS v0.6 exists to stop architecture drift. The project is not trying to become a normal app that controls other apps. The goal is still that Jarvis is the iPhone XR.

## Decision Hierarchy

### Level 0: Normal App

- What Jarvis controls: its own app process, screen, and allowed permissions.
- What iOS still controls: Home Screen, lock screen, app switching, system buttons, background policy.
- Feels like Jarvis is the phone: no.
- Offline viability: good inside the app only.
- Spotify/browser: can exist, but this drifts into generic app orchestration.
- Required: installable native app.
- Can be built now: yes.
- Blocked: device identity, system ownership, preventing casual exit.
- Recommendation: rejected as the main project.

### Level 1: Native Jarvis Shell

- What Jarvis controls: full-screen Jarvis interface, local tools, camera panels, voice surface, memory.
- What iOS still controls: Home Screen, lock screen, app switching, system buttons, permissions.
- Feels like Jarvis is the phone: partial while foreground.
- Offline viability: strong while foreground.
- Spotify/browser: optional modules only.
- Required: native iOS build path and permissions.
- Can be built now: after build toolchain decision.
- Blocked: true home ownership, lock ownership, background identity.
- Recommendation: useful foundation, rejected as final identity because it remains an app.

### Level 2: Restricted Jarvis Device

- What Jarvis controls: visible device purpose, reduced clutter, offline Jarvis tools.
- What iOS still controls: Home Screen mechanics, lock screen, system buttons, escape paths.
- Feels like Jarvis is the phone: moderate if disciplined.
- Offline viability: strong.
- Spotify/browser: optional modules, not identity.
- Required: delete apps, Screen Time, Focus, Home Screen cleanup, no SIM.
- Can be built now: yes.
- Blocked: enforcement against casual exit.
- Recommendation: immediate preparation only.

### Level 3: Supervised Jarvis Kiosk

- What Jarvis controls: foreground device experience and a single visible Jarvis surface.
- What iOS still controls: kernel, secure boot, permission framework, system internals.
- Feels like Jarvis is the phone: strong while locked.
- Offline viability: strong.
- Spotify/browser: constrained because external app escape conflicts with kiosk mode.
- Required: supervised Single App Mode or Guided Access, native Jarvis shell, recovery plan.
- Can be built now: yes if setup exists.
- Blocked: SpringBoard hooks, lock screen hooks, global button remaps.
- Recommendation: strongest non-jailbreak approximation.

### Level 4: Managed Jarvis Appliance

- What Jarvis controls: dedicated appliance behavior, app allow lists, restrictions, automatic relaunch where possible, offline tools.
- What iOS still controls: SpringBoard internals, lock screen internals, secure boot, root restrictions.
- Feels like Jarvis is the phone: very close for practical use.
- Offline viability: strong.
- Spotify/browser: optional and restricted, not identity.
- Required: supervision, configuration profiles or MDM-style controls, native Jarvis shell, recovery profile.
- Can be built now: yes only if supervision tooling exists.
- Blocked: SpringBoard hooks, true daemon, arbitrary app inspection.
- Recommendation: best current non-jailbreak target.

### Level 5: Jailbroken JarvisOS

- What Jarvis controls: SpringBoard hooks, lock screen hooks, daemon, button remaps where possible, system UI control where tested.
- What iOS still controls: secure boot chain, hardware firmware, SEP, signed firmware.
- Feels like Jarvis is the phone: yes, if hooks are real and stable.
- Offline viability: strongest.
- Spotify/browser: secondary flows if hooks and policy allow.
- Required: verified XR iOS 18.7.9 jailbreak, Theos or equivalent toolchain, device tests, safe rollback.
- Can be built now: no.
- Blocked: no verified jailbreak route in this repo, A12 is not checkm8, system hooks are unproven.
- Recommendation: true goal, preserved as waiting lane.

### Level 6: Firmware Or Custom OS Replacement

- What Jarvis controls: not practically available.
- What iOS still controls: Apple secure boot, firmware signing, SEP, hardware bring-up.
- Feels like Jarvis is the phone: theoretical only.
- Offline viability: not relevant.
- Spotify/browser: not relevant.
- Required: custom signed firmware or broken secure boot chain.
- Can be built now: no.
- Blocked: Apple secure boot and signing.
- Recommendation: impossible or not practical for iPhone XR.

## Gate Decision

The current iPhone XR cannot meet true JarvisOS ownership now without a verified jailbreak. The next decision is one of:

- Build managed appliance mode.
- Pause system ownership work until jailbreak feasibility changes.
- Change hardware or iOS target to something with a verified jailbreak route.
