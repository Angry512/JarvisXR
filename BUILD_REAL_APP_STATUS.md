# Build Real App Status

## Created

- Real native Swift/UIKit JarvisXR app project created under `ios/JarvisXR`.
- GitHub Actions macOS build workflow created at `.github/workflows/ios-build.yml`.
- Windows sideload path created in `docs/WINDOWS_INSTALL_XR.md`.
- Troubleshooting guide created in `docs/BUILD_AND_SIDELOAD_TROUBLESHOOTING.md`.
- v1.1 hardening added stronger router commands, local memory behavior, speech controls, diagnostics, settings actions, first-run safety prompt, keyboard-safe UI, Swift tests, and first-run XR test docs.
- Final pass added premium UIKit components, improved main-screen instrument layout, Windows tkinter preview, preview self-test, Identity screen, additional command coverage, and final install checklist.
- Overhaul pass removed visible XR branding from the product UI, strengthened the orb, added orb states, added voice profiles, improved the Windows preview, and added the approval checklist.
- Visual reference pass copied the Gemini orb reference into `assets/visual_reference`, generated square/icon-oriented derivatives, rebuilt the native orb as a layered cyan instrument, upgraded the Windows tkinter orb, and added `docs/JARVIS_VISUAL_SYSTEM.md`.
- Control Mesh pass added `jarvis://` deep-link intake, App Intents source, an in-app Control Mesh setup screen, smarter system-control command responses, Control Pack setup files, and Windows preview Control Mesh behavior.
- Primary post-install correction rebuilt the real iPhone home screen as a full-screen voice-first JARVIS surface, removed Recent Activity and the large response panel, added in-app push-to-talk speech recognition, changed the default voice to Natural, added real Vision OCR/barcode analysis after capture, and generated a real orb-based app icon.
- Follow-up intelligence pass added natural command phrasing, stronger Control Mesh routing, object-model readiness detection, a Core ML model drop-in folder, inspection speech summaries, profile preview, and guarded Personal Voice authorization support.
- Real-device bugfix gate added compact keyboard mode for the 414 x 896 phone surface, restored obvious `JARVIS ready` orb feedback, added speech endpoint timers, added a small assistant core/state model, and rebuilt the Windows preview as a phone-frame approval gate.
- Product UI correction pass removed product-facing tester copy from the app surface, added the top-right help circle, separated the Windows phone surface from external Preview controls, and created a local approval bundle under `dist/jarvis_local_approval_bundle`.
- Final release-candidate pass added a deterministic command planner, Control Mesh planner, clearer Mesh top control, stronger help content, model-gated inspection language, final guardrails, and release-candidate bundle notes.
- Production pass added product-only preview mode, Mesh sheet preview, production visual-state reports, product surface regression tests, design-system tokens, and safer Mesh/Return App Intents.

## Verified Locally

- Repository Python validation and tests can run on Windows.
- Project files exist for XcodeGen-based macOS build.
- `xcodebuild` is not available on this Windows machine.
- `xcodegen` is not available on this Windows machine.
- The native app build must be verified by GitHub Actions on macOS.
- The Windows preview can run before GitHub upload with `python preview/windows_jarvis_preview/jarvis_preview.py`.
- The preview self-test can run with `python preview/windows_jarvis_preview/jarvis_preview.py --self-test`.
- The interaction gate can run with `python tools/jarvis_interaction_test.py`.
- The local approval bundle can run the preview and tests from `dist/jarvis_local_approval_bundle`.
- The final release-candidate bundle adds `screens_to_review.md`, `known_limits.md`, and `final_release_candidate_notes.md`.
- The production approval bundle adds `run_visual_review.bat`, `production_review_steps.md`, and `do_not_push_until.md`.
- Do not push or rebuild the IPA until the Windows phone-frame preview is approved locally.
- Visual assets can be regenerated with `python tools/prepare_visual_assets.py`.
- Deep links can be tested after install through Shortcuts using `jarvis://command?text=system%20check`, `jarvis://inspect`, `jarvis://diagnostics`, and related URLs.

## Must Be Verified In GitHub Actions

- XcodeGen installs.
- `JarvisXR.xcodeproj` generates.
- `xcodebuild` builds `JarvisXR.app` for iphoneos with code signing disabled.
- `JarvisXR-unsigned.ipa` is packaged and uploaded.
- Optional simulator tests run and upload `test.log` if available.

Workflow name:
`Build JarvisXR iOS IPA`

Expected artifact:
`JarvisXR-unsigned-ipa`

Expected IPA:
`JarvisXR-unsigned.ipa`

## Must Be Verified On XR

- AltServer installs the IPA.
- JarvisXR launches.
- Visible product UI says `JARVIS`.
- Control Mesh screen opens.
- Shortcuts can call `jarvis://` links.
- App Intents compile and appear only after GitHub Actions/Xcode verifies them.
- Commands work.
- Notes persist.
- Speech works.
- Camera permission and capture path work.
- Push-to-talk orb listening asks for microphone and Speech permission, then routes recognized text through the local command router.
- Orb tap flow must be verified: Standby, JARVIS ready, Listening, Heard you, Processing, Speaking, Done.
- Keyboard mode must be verified: input remains above the keyboard, orb/state remain visible, and compact mode feels intentional.
- Natural phrases such as `Jarvis, look at this`, `remember this`, `show me how to tap that`, `play music`, and `make the screen darker` route correctly.
- Listening, Processing, Speaking, Inspection, Quiet, Standby, and Blocked states are visually distinct.
- App icon shows the JARVIS orb and is not blank.
- Vision OCR and barcode scan after capture report real results when present.
- Object detection reports model missing until a compiled Core ML model is bundled and tested.
- Personal Voice can request authorization on supported iOS versions, but no custom voice is trained or uploaded.
- Diagnostics screen opens.
- Guided Access locks to JarvisXR and exits safely.

First-run script:
`docs/XR_FIRST_RUN_TEST_SCRIPT.md`

Final checklist:
`docs/FINAL_TODAY_CHECKLIST.md`

Approval checklist:
`docs/APPROVAL_CHECKLIST_BEFORE_UPLOAD.md`

## Boundaries

No jailbreak is claimed. No true OS ownership is claimed. Guided Access is the lockdown layer after install. Control Mesh uses official iOS layers: Voice Control, Vocal Shortcuts, Shortcuts, URL schemes, App Intents where verified, Switch Control, and AssistiveTouch. The app is visually branded as `JARVIS`; `JarvisXR` remains a technical project and bundle name only.
