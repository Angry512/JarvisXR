# Build And Sideload Troubleshooting

## GitHub Actions Workflow Fails

- Open the failed step.
- Download build logs if available.
- Check whether XcodeGen installed.
- Check whether Xcode version supports iOS 18 builds.
- Check `JarvisXR-build-output` for `build.log`, `schemes.log`, `test.log`, and `BUILD_REAL_APP_STATUS.md`.
- If the preview works but GitHub Actions fails, treat the preview as UI evidence only. The IPA still requires the macOS workflow to pass.

## Windows Preview Fails

- Run `python preview/windows_jarvis_preview/jarvis_preview.py --self-test`.
- Confirm Python includes tkinter.
- If speech does not work in preview, continue. Preview speech only uses optional local `pyttsx3` if already installed.
- The preview is not required for IPA packaging, but it is useful for approving the experience before upload.

## Xcode Project Generation Fails

- Check `ios/JarvisXR/project.yml`.
- Confirm XcodeGen installed in the workflow.
- Confirm source paths exist.

## Scheme Missing

- Confirm `xcodegen generate` completed.
- Confirm the scheme is named `JarvisXR`.
- Confirm `JarvisXR.xcodeproj` was generated in `ios/JarvisXR`.

## xcodebuild Fails

- Read `build.log`.
- Check Swift compile errors.
- Check deployment target.
- Check missing framework imports.
- Do not add signing claims to fix compile errors.
- If simulator tests fail but the device build succeeds, inspect `test.log`. The unsigned IPA path is still controlled by the iPhoneOS build and package steps.

## Unsigned IPA Not Created

- Confirm `JarvisXR.app` exists under `build/DerivedData/Build/Products/Release-iphoneos`.
- Confirm `Payload/JarvisXR.app` was created.
- Confirm zip created `JarvisXR-unsigned.ipa`.
- If packaging fails, read `BUILD_REAL_APP_STATUS.md` in the workflow artifact.

## Sideloadly Cannot Detect Phone

- Unlock the XR.
- Try another USB cable.
- Install Apple Devices or iTunes support.
- Tap Trust This Computer.
- Restart Sideloadly.

## Trust Computer Issue

- Disconnect and reconnect USB.
- Unlock the XR before connecting.
- Reset trust settings only if needed.

## Apple ID Verification Issue

- Confirm credentials.
- Complete any Apple ID security prompt.
- Use the same Apple ID intentionally chosen for sideloading.

## App Expires After 7 Days

- Refresh with Sideloadly.
- Reinstall the latest IPA artifact.
- This is expected with free Apple ID sideloading.

## App Opens Then Crashes

- Reinstall from the latest artifact.
- Check whether the IPA came from a successful workflow run.
- Check GitHub Actions build logs.
- If it crashes after camera permission, reopen JarvisXR and test Diagnostics before opening Camera again.
- Report the last command or screen used before the crash.

## Camera Permission Issue

- Open iOS Settings.
- Find JarvisXR.
- Enable Camera.
- Relaunch JarvisXR.

## Speech Issue

- Check mute switch and volume.
- Open JarvisXR Settings.
- Enable Speech Output.
- Try `speak this system check`.

## Guided Access Exit Issue

- Test exit before relying on Guided Access.
- Use the configured Guided Access passcode or Face ID exit.
- Do not start Guided Access if the exit path is unclear.
- See `docs/GUIDED_ACCESS_LOCKDOWN_AFTER_INSTALL.md`.
