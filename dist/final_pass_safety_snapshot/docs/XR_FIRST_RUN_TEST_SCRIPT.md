# XR First Run Test Script

Run this before enabling Guided Access.

1. Open JARVIS.
2. Confirm the app does not crash.
3. Read the first-launch safety prompt.
4. Confirm the visible title is `JARVIS`.
5. Confirm it uses the full phone screen and does not show Recent Activity.
6. Confirm the top-right `?` help circle is visible.
7. Open help and confirm it explains voice, typing, vision, states, and limits.
8. Confirm the orb animates and the state says Standby.
9. Tap the orb once and confirm the state says `JARVIS ready`.
10. Tap the orb again. Accept microphone and Speech permission if iOS asks.
11. Say `scan this`, then pause.
12. Confirm Listening, Heard you, Processing, and Inspection are visible in sequence.
13. Tap the command field and confirm compact keyboard mode keeps the input, orb, state, and help icon visible.
14. Hide the keyboard and confirm the full orb layout returns.
15. Type `help`.
16. Type `scan this`.
17. Accept camera permission.
18. Capture a frame and check whether text or barcode results appear if present.
19. Type `read this`.
20. Type `detect objects` and confirm JARVIS says a Core ML model is required.
19. Type `Jarvis, look at this`.
20. Type `remember this test note`.
21. Type `show notes`.
22. Type `show me how to tap that`.
23. Type `control mesh`.
24. Type `show grid`, `tap`, and `scroll down`.
25. Type `companion mode` and confirm it does not claim arbitrary floating UI.
26. Open Diagnostics from Menu.
27. Open Settings from Menu and confirm voice profile, profile preview, and Personal Voice status text.
28. Create a test Shortcut that opens `jarvis://command?text=system%20check`.
29. Run the Shortcut and confirm JARVIS receives it.
30. Create a test Shortcut that opens `jarvis://inspect`.
31. Enable Voice Control and test Show Grid, Tap, Scroll Down, and Go Home.
32. Close and reopen JARVIS.
33. Confirm notes still appear.
34. Turn Wi-Fi off.
35. Test `status`, `show notes`, and `time`.
36. Enable Guided Access only after the app and exit path are tested.
37. Triple-click the side button to start Guided Access.
38. Triple-click again and confirm exit works.

Report back:

- Whether JARVIS launched.
- Whether AltServer installed without errors.
- Whether speech worked.
- Whether push-to-talk recognition worked.
- Whether camera permission and capture worked.
- Whether OCR or barcode scan found anything on a suitable test object.
- Whether `jarvis://` Shortcuts reached JARVIS.
- Whether Voice Control global commands worked.
- Whether a Vocal Shortcut phrase worked.
- Whether notes survived app restart.
- Whether Guided Access started and exited safely.
- Any crash message or failed command.
