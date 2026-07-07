# Preview Notes

Run:

```powershell
dist\jarvis_local_approval_bundle\run_preview.bat
```

The left phone frame is the product surface. Judge only that surface for visual approval.

The right panel is an external review harness. It exists to trigger states without rebuilding the iPhone app. It is not part of the final phone UI.

The top-left Mesh control represents JARVIS Control Mesh: official iOS routes through Voice Control, Shortcuts, URL routes, and user-guided steps.

Use the external `Product-only view` control to hide the review harness and judge the phone surface by itself.

Important limits:

- This is not an iOS Simulator.
- This does not compile Swift.
- This does not prove camera, microphone, Speech framework, or Guided Access behavior on the phone.
- It does prove that the local phone-frame layout, state flow, help affordance, and command priorities are coherent before GitHub upload.
- It can export text visual-state reports through `run_visual_review.bat`.
