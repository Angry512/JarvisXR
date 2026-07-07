# Production Product Audit

## 1. Current Strengths

- `JarvisRootViewController.swift` keeps the main surface voice-first: wordmark, orb, state, transient line, command bar, Help, and Mesh.
- `JarvisHelpViewController.swift` has concise sections and no developer panels.
- `JarvisCameraViewController.swift` uses AVFoundation, Apple Vision OCR, barcode scanning, torch, focus, exposure, and a scan overlay.
- `JarvisCommandPlan.swift` and `JarvisControlMeshPlanner.swift` now give the router a deterministic planning layer.
- `preview/windows_jarvis_preview/jarvis_preview.py` separates phone surface from external controls.
- `tools/jarvis_interaction_test.py` protects the core visual and routing promises.

## 2. Current Visual Weaknesses

- The Windows preview still needs stronger production framing: product-only mode, Mesh sheet, and state reports.
- Mesh is clearer than ellipsis, but needs more visible meaning in preview and help.
- The preview orb is good mechanically, but needs more state-specific glow and stronger inspection energy.

## 3. Current UX Weaknesses

- The review harness can still dominate the first impression if the user focuses on the right panel.
- Control Mesh needs to feel like a command surface, not a limitation page.
- Inspection should lead with scan language instead of camera utility language.

## 4. Current Architecture Weaknesses

- The planner is present, but source-level tests should lock down its route categories and model-gated object detection behavior.
- Preview state coverage should be exported into review artifacts so visual approval is not memory-based.

## 5. Current Local Preview Weaknesses

- No product-only toggle yet.
- No Mesh sheet state in the phone frame.
- No generated visual-state reports for idle, listening, speaking, keyboard, help, Mesh, inspection, permission denied, and model missing.

## 6. Phone Controller Illusion Weaknesses

- JARVIS cannot actually own iOS without jailbreak or private APIs.
- The illusion must come from fast command routing, confident Control Mesh instructions, return-to-JARVIS routes, and Guided Access appliance mode.

## 7. Accessibility Risks

- Top controls must remain understandable by label: Mesh and Help.
- State text must not rely only on color.
- Command input and Send must remain reachable in keyboard mode.
- Preview tests should keep protecting help, Mesh, orb, state, input, and Send.

## 8. Keyboard Risks

- Compact mode can feel compressed on 414 x 896 if the orb or state shifts too low.
- Required elements must remain visible: Mesh, Help, JARVIS, orb, state, command input, Send.

## 9. State Clarity Risks

- Listening and Speaking must remain visually distinct.
- Permission denied and no speech must not feel like crashes.
- Done should settle back toward readiness.

## 10. What Must Not Be Broken

- No Recent Activity.
- No large response panel.
- No debug chips.
- No product-facing JSON.
- No visible device suffix in product UI.
- No fake object detection claim.
- No private API or jailbreak implementation.

## 11. What Should Be Built In This Pass

- Product-only preview mode.
- Mesh sheet in preview.
- Visual-state export tool.
- Product surface regression test.
- Release-candidate bundle commands for visual review.
- More explicit Control Mesh Commander artifacts.

## 12. Impossible Without Jailbreak Or Private APIs

- SpringBoard hooks.
- Lock screen hooks.
- Hidden global taps.
- Global screen reading.
- Background wake word.
- Root daemon behavior.
- Arbitrary floating overlay over other apps.

## 13. Exact Target

JARVIS should feel like a premium iPhone command surface: central orb, vision-first command routing, confident Mesh controller language, honest public-iOS boundaries, and a local preview trustworthy enough for visual approval before any GitHub build.
