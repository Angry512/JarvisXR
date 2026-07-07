# Approval Checklist Before Upload

Run the Windows preview:

```powershell
python preview/windows_jarvis_preview/jarvis_preview.py
```

Run the preview self-test:

```powershell
python preview/windows_jarvis_preview/jarvis_preview.py --self-test
```

Run the interaction self-test:

```powershell
python tools/jarvis_interaction_test.py
```

Approve these before GitHub upload:

1. Confirm title says `JARVIS` only.
2. Confirm orb looks premium.
3. Confirm orb animates.
4. Confirm command input works.
5. Toggle Keyboard and confirm input remains above the keyboard.
6. Confirm the orb and state line remain visible in keyboard mode.
7. Confirm the top-right help circle opens help.
8. Confirm help explains voice, typing, vision, states, and limits.
9. Confirm there is no guide text, checklist text, developer wording, report output, or data dump in the phone frame.
10. Confirm the full orb returns when keyboard mode closes.
11. Tap Orb once and confirm `JARVIS ready`.
12. Tap Orb again and confirm Listening.
13. Use `Speak: scan this` and confirm Heard you, Processing, and Inspection.
14. Confirm no Recent Activity or large response panel is on the home screen.
15. Confirm orb listening, processing, and speaking states look different.
16. Confirm inspection mode changes state.
17. Confirm no visible device suffix is present in product UI.
18. `help` returns inspection-first commands.
19. `scan this`, `look at this`, `read this`, and `detect objects` route to inspection truthfully.
20. `detect objects` reports model missing unless a real Core ML model is bundled.
21. `control mesh`, `show grid`, `tap`, and `scroll down` route to official control layers.
22. `companion mode` does not claim arbitrary floating UI.
23. `remember this`, `show notes`, and `search notes field` work.
24. Settings can preview voice profiles and report Personal Voice authorization status.
25. The app icon is the orb, not the default icon.
26. No jailbreak, root, SpringBoard, lock screen, launchd, arbitrary app control, or true OS takeover is claimed.

After approval:

1. Only after local approval, upload or push the repo to GitHub.
2. Run `Build JarvisXR iOS IPA`.
3. Download `JarvisXR-unsigned-ipa`.
4. Install `JarvisXR-unsigned.ipa` with AltServer.
5. Run the first-run script before enabling Guided Access.
