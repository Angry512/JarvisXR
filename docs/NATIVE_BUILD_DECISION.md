# Native Build Decision

This is the next real decision before the XR can run Jarvis.

## A. Mac/Xcode Available

- Can do: build native iOS shell, use free signing for development install, test on XR.
- Cannot do: claim jailbreak hooks, install launchd daemon on stock iOS.
- Guided Access: usable once app is installed.
- Single App Mode: possible if Apple Configurator or supervision path is also available.
- Native app install: realistic.
- Project should pause: no, proceed to build minimal native shell.

## B. Mac/Xcode Not Available

- Can do: maintain repo, run tests, prepare assets, prepare specs.
- Cannot do: fully build and install native iOS app from Windows alone.
- Guided Access: only useful once an app exists on the phone.
- Single App Mode: not available from Windows alone.
- Native app install: not realistic from this path alone.
- Project should pause: yes, until build path exists.

## C. Apple Configurator Available

- Can do: supervise device, prepare Single App Mode route, apply stronger restrictions.
- Cannot do: replace iOS, create SpringBoard hooks.
- Guided Access: available.
- Single App Mode: available if the Jarvis app exists.
- Native app install: requires app build and signing path too.
- Project should pause: no if Xcode or signing path also exists.

## D. Only Windows And Raspberry Pi Available

- Can do: run Jarvis Core tests, maintain repo, prepare docs, use restricted Home Screen fallback.
- Cannot do: fully build and install native iOS app, supervise through Apple Configurator from Windows alone.
- Guided Access: only useful once Jarvis shell is installed.
- Single App Mode: no.
- Native app install: not realistic.
- Project should pause: yes, after physical restriction setup.
