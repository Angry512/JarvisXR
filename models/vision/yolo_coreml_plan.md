# YOLO Core ML Plan

1. Choose a nano or small detector.
2. Export to Core ML if the toolchain and target iOS version support it.
3. Test static frames first.
4. Limit input resolution.
5. Measure latency, heat, and battery.
6. Attempt low-FPS live detection only after static tests pass.
