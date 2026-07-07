# Final Today Checklist

1. Run the Windows preview:
   `python preview/windows_jarvis_preview/jarvis_preview.py`
2. Confirm the preview title says `JARVIS` only.
3. Confirm the orb looks premium, layered, and animated.
4. Run the preview self-test:
   `python preview/windows_jarvis_preview/jarvis_preview.py --self-test`
5. Run `python tools/prepare_visual_assets.py`.
6. Run `docs/APPROVAL_CHECKLIST_BEFORE_UPLOAD.md`.
7. Upload or push the changed repo files to GitHub.
8. Open GitHub Actions.
9. Run `Build JarvisXR iOS IPA`.
10. Download the `JarvisXR-unsigned-ipa` artifact.
11. Extract `JarvisXR-unsigned.ipa`.
12. Open Sideloadly on Windows.
13. Connect the iPhone XR by USB and trust the computer.
14. Select the XR and `JarvisXR-unsigned.ipa`.
15. Install with the Apple ID selected for sideloading.
16. Trust the developer profile on the XR if iOS asks.
17. Open JARVIS.
18. Test `help`.
19. Test `system check`.
20. Test `battery`.
21. Test `save note first field test`.
22. Test `show notes`.
23. Test `voice test`.
24. Test `voice quiet`.
25. Test Camera and accept permission.
26. Test Diagnostics.
27. Test Settings and Identity.
28. Turn Wi-Fi off and test local commands again.
29. Enable Guided Access only after the app and exit path work.
30. Triple-click the side button to start Guided Access.
31. Triple-click again and verify exit.

Stop and report the exact error if the workflow fails, Sideloadly fails, the app crashes, camera permission fails, speech fails, notes do not persist, or Guided Access exit is unclear.
