# Windows Install XR

This path installs the GitHub Actions unsigned IPA onto the iPhone XR from Windows using Sideloadly.

## Requirements

- Windows PC.
- USB cable.
- iPhone XR on iOS 18.7.9.
- Wi-Fi optional after install.
- Apple ID for sideloading.
- Sideloadly.
- Apple Devices or iTunes support if Sideloadly requires Apple mobile drivers.

## Build The IPA

Before upload, run the Windows preview:

```powershell
python preview/windows_jarvis_preview/jarvis_preview.py
python preview/windows_jarvis_preview/jarvis_preview.py --self-test
```

1. Push this repo to GitHub.
2. Open the GitHub repository.
3. Go to Actions.
4. Run `Build JarvisXR iOS IPA`.
5. Wait for the workflow to finish.
6. Open the completed workflow run.
7. Download the `JarvisXR-unsigned-ipa` artifact.
8. Extract the artifact if GitHub downloads it as a zip.
9. Locate `JarvisXR-unsigned.ipa`.

## Install With Sideloadly

1. Install Sideloadly on Windows.
2. Install Apple Devices or iTunes support if the phone is not detected.
3. Connect the XR by USB.
4. Unlock the XR.
5. Tap Trust This Computer on the XR if prompted.
6. Open Sideloadly.
7. Select the XR.
8. Select `JarvisXR-unsigned.ipa`.
9. Enter the Apple ID used for sideloading.
10. Start install.
11. If iOS asks, trust the developer profile on the XR.
12. Open JARVIS.
13. Confirm the visible title says `JARVIS`.
14. Confirm the orb animates before enabling Guided Access.

## First Tests On XR

Use `docs/XR_FIRST_RUN_TEST_SCRIPT.md` for the full first-run test.
Use `docs/FINAL_TODAY_CHECKLIST.md` for the complete upload, build, install, and lockdown sequence.

Minimum smoke test:

1. Run `help`.
2. Run `status`.
3. Run `battery`.
4. Run `save note first field test`.
5. Run `show notes`.
6. Test `voice test`.
7. Test `voice quiet`.
8. Run `normal mode`.
9. Open Camera and grant camera permission.
10. Open Diagnostics.
11. Open Settings and review Guided Access instructions.
12. Enable Guided Access only after the app and exit path work.

## Expiration

Free Apple ID sideloaded apps usually expire after 7 days and need refresh.

## Boundaries

No jailbreak tools are used. JarvisXR does not claim root access, SpringBoard hooks, lock screen hooks, launchd daemon install, arbitrary app control, or true OS takeover.
