# Final Release Candidate Notes

This bundle is for local review only.

What changed:

- The phone frame is the product surface.
- Mesh is the named controller entry point.
- The `?` help sheet explains operation and limits.
- Product-only view lets the user judge the phone frame without external controls.
- Visual-state reports are generated under `dist/production_visual_review`.
- Scan, read, look, and detect are the primary command routes.
- Phone-level commands route through Control Mesh instead of pretending to control iOS directly.
- Object detection is model-gated.

Do not use this bundle as proof of Swift compilation or phone behavior. GitHub Actions is still required for macOS build verification.
