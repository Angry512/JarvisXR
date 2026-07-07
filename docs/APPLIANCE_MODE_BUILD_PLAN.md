# Appliance Mode Build Plan

This is what must exist before the XR can be truly used as Jarvis in appliance mode.

## Required Jarvis Pieces

- Native Jarvis shell.
- Camera inspection.
- Voice command interface.
- Local memory.
- Offline utilities.
- Sensor tools.
- Local TTS.
- Local or limited STT.
- Core ML and Vision modules later.
- Guided Access setup.
- Single App Mode setup if Mac exists.

## Current Limit

This repo does not currently produce an installable iOS app.

Building and installing the native shell requires a real iOS build path. Likely options are Mac/Xcode with free signing or another legitimate signing path.

Windows alone cannot fully build and install a native iOS app.

## Practical Order

1. Confirm build environment.
2. Choose native app path.
3. Build minimal Jarvis shell.
4. Install on XR.
5. Test Guided Access.
6. Test Single App Mode only if supervision exists.
7. Test offline behavior.
