# Offline Vision v0.4

This plan does not claim any model runs on iPhone 6 yet.

## Strategy

Use small, narrow models and classical image utilities. The iPhone 6 target is not suitable for large vision-language models.

## YOLO Nano Or Small

- Start with nano or small object detection models.
- Limit label set and input resolution.
- Prefer still-image detection first.
- Treat live detection as later low-FPS mode only after thermal and battery tests.

## Core ML Export

- Convert candidate models to Core ML only after target iOS version is known.
- Validate model format, minimum iOS version, and runtime memory requirements.
- Keep original model, conversion script, model card, and test images in dock/build tooling.

## OCR

- Begin with still-frame OCR.
- Evaluate iOS-version-compatible local OCR or jailbreak-friendly libraries.
- Use dock mode for heavier OCR when local quality is not acceptable.

## QR And Barcode

- Prioritize QR and barcode ahead of heavier detection.
- They are practical offline tools and useful for field mode.

## Document Edges

- Use classical image utilities for edge detection, crop, contrast, rotation, and color sampling.
- These should be offline and fast.

## iPhone 6 Constraints

- Target small model files under 20 MB when possible.
- Prefer latency under 500 ms for still-image utilities.
- Object detection under 1500 ms may be acceptable for manual scan.
- Avoid constant live inference until battery and thermal tests prove it safe.

## Windows Now

- Test model conversion scripts.
- Test static image inference on PC.
- Build adapter contracts and fixture outputs.
- Validate registry to adapter mapping.

## Requires iPhone Hardware

- Camera frame capture path.
- Core ML runtime performance.
- Thermal and battery behavior.
- Low memory failure modes.

## Requires Exact iOS Version

- Core ML compatibility.
- Vision framework availability.
- OCR framework availability.
- Build and signing route.

## Avoid

- Cloud-only vision.
- Large VLMs.
- Continuous high-FPS inference.
- Claims of field reliability before hardware testing.
