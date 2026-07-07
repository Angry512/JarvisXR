# Windows Preview Guide

Run this before pushing or rebuilding the IPA:

```powershell
python preview/windows_jarvis_preview/jarvis_preview.py
```

Run the automated preview checks:

```powershell
python preview/windows_jarvis_preview/jarvis_preview.py --self-test
python tools/jarvis_interaction_test.py
```

## What This Preview Tests

- Phone-sized 414 x 896 portrait surface.
- Safe area top and bottom.
- Product-only phone frame with no tester text.
- Named Mesh control for phone-level routes.
- Top-right help circle and help sheet.
- Keyboard open and closed modes.
- Compact command mode with smaller orb.
- Input staying above the keyboard.
- Orb tap flow: Standby, JARVIS ready, Listening.
- Simulated speech endpoint: Heard you, Processing, Inspection.
- Priority commands: look at this, scan this, read this, detect objects.

## What To Approve Locally

1. Judge the left phone frame as the product surface.
2. Confirm it says `JARVIS` only.
3. Confirm there is no guide text, checklist text, developer text, report output, or data dump inside the phone frame.
4. Tap the top-right `?` and confirm help opens.
5. Confirm the top-left Mesh control is understandable.
6. Tap Orb once. State should become `JARVIS ready`.
7. Tap Orb again. State should become Listening.
8. Click `Speak: scan this`. State should move to Inspection after the endpoint.
9. Click `Keyboard`. Input should remain above the keyboard.
10. The Mesh control, help icon, orb, state line, input, and Send should remain visible in keyboard mode.
11. Click Look at this, Scan this, Read this, and Detect objects.
12. Detect objects should state that the object model is not installed and text/code scanning remain active.

## What It Does Not Prove

- It does not run an iOS Simulator.
- It does not compile Swift.
- It does not test the real iPhone camera, microphone, Speech framework, or Guided Access.
- It does not prove phone success until the rebuilt app is installed and tested on the iPhone.

Do not push or rebuild for the phone until this preview feels better on the laptop.

## Local Approval Bundle

Use:

```powershell
dist/jarvis_local_approval_bundle/run_preview.bat
dist/jarvis_local_approval_bundle/run_tests.bat
```

Read:

- `dist/jarvis_local_approval_bundle/approval_checklist.md`
- `dist/jarvis_local_approval_bundle/latest_test_report.txt`
- `dist/jarvis_local_approval_bundle/what_to_check_before_github.md`
- `dist/jarvis_local_approval_bundle/screens_to_review.md`
