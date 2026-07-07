# iPhone XR Device Mode Pivot

## What Changed

Versions v0.1 through v0.4 assumed an iPhone 6 jailbreak-first path. That work created the planning foundation, daemon harness, adapter architecture, native UIKit skeletons, and the future SpringBoard tweak lane.

The active target is now:

- Device: iPhone XR
- iOS: 18.7.9
- SIM: none
- Cellular dependence: none
- Wi-Fi: optional online enhancement
- Spotify: already installed

## Why The Pivot Helps

iPhone XR is stronger than the original iPhone 6 target. Its A12 Bionic chip, newer camera path, better battery, larger screen, and stronger Core ML headroom make it a better Jarvis device for native AI, camera inspection, local sensing, offline utilities, and polished voice or vision experiments.

## Jailbreak Reality

The repo now treats XR iOS 18.7.9 jailbreak ownership as blocked pending verified support. SpringBoard hooks, launchd daemon install, root access, lock screen hooks, and system-wide button remaps remain preserved as a future lane, but they are not claimed for this device.

## New Practical Method

The current path is Jarvis Device Mode:

- Native iOS Jarvis shell as the foreground identity.
- Device stripped down so Jarvis is the only visible purpose.
- Supervised Single App Mode as the strongest non-jailbreak ownership route.
- Guided Access as fallback when supervision is unavailable.
- Shortcuts and App Intents as integration bridges.
- Controlled Spotify and browser/search flows.
- Raspberry Pi and Windows PC retained as dock, build, sync, backup, recovery, and model-conversion tools.

This is not a normal app strategy. It is a device ownership strategy built inside the limits of stock iOS until a verified jailbreak lane exists.

This is not a web app strategy. The product remains a native Jarvis device experience.
