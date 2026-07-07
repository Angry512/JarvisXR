# Supervised Single App Mode Plan

Single App Mode is the strongest non-jailbreak path for Jarvis to own the device experience.

## Requirement

Single App Mode requires the device to be supervised through Apple Configurator or an MDM-style setup path. This may require a Mac or a supported MDM route. The repo must not pretend Windows alone can supervise the device.

## Intended Result

Once supervised and configured, the iPhone XR should lock into the native Jarvis app. Home Screen browsing, app switching, and casual app use should no longer define the device.

## Guided Access Fallback

If supervision is unavailable, Guided Access is the immediate fallback. It is useful for manual lockdown, but it is not the preferred ownership path.

## Spotify And Browser Constraint

Single App Mode locks to one app. That means browser/search and Spotify need one of these designs:

- Jarvis-native module.
- In-app browser or controlled web search view.
- Approved integration through App Intents, Shortcuts, URL schemes, or SDK paths.
- Soft Ownership Mode when external app handoff is desired.

Strict Single App Mode can conflict with external Spotify or Safari use. v0.5 documents that conflict rather than hiding it.

## Setup Checklist

- Confirm whether a Mac with Apple Configurator is available.
- Confirm whether an MDM-style path is available.
- Install or sideload native Jarvis app once a build path is chosen.
- Supervise the iPhone XR.
- Apply Single App Mode to the Jarvis bundle identifier.
- Test reboot, lock, unlock, app relaunch, camera permission, microphone permission, and recovery exit.
