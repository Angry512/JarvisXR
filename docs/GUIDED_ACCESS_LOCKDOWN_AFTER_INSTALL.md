# Guided Access Lockdown After Install

Do not enable Guided Access until JarvisXR opens and the exit path has been tested.

## Enable

1. Open iOS Settings.
2. Open Accessibility.
3. Open Guided Access.
4. Turn Guided Access on.
5. Set a Guided Access passcode.
6. Enable Face ID exit only if you want that recovery path.

## Lock To JarvisXR

1. Open JarvisXR.
2. Run `help`, `system check`, `battery`, `show notes`, and `guided access`.
3. Triple-click the side button.
4. Tap Start.
5. Confirm JarvisXR stays in the foreground.

## Test Exit

1. Triple-click the side button.
2. Enter the Guided Access passcode or use the configured Face ID exit.
3. End Guided Access.
4. Reopen JarvisXR and confirm it still works.

## What This Achieves

- Keeps JarvisXR in the foreground during use.
- Makes the XR feel like a dedicated Jarvis appliance.
- Reduces casual exits into the normal iOS environment.

## What This Does Not Achieve

- No jailbreak.
- No root access.
- No SpringBoard hooks.
- No lock screen hooks.
- No launchd daemon install.
- No arbitrary app control.
- No true OS takeover.
