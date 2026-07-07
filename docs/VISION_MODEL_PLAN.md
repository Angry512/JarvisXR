# Vision Model Plan

## Hardware Reality

iPhone 6 hardware is limited. Large vision-language models are not a practical offline target. The usable path is small, narrow models and classical computer vision utilities.

## Object Detection

Start with static image detection. Export YOLO nano or small-style models to Core ML only after confirming toolchain compatibility. Target low resolution, low frequency, and clear labels. Low-FPS live detection can come later if thermal and battery tests allow.

## OCR

Evaluate old-iOS-compatible OCR options and jailbreak-friendly native libraries. Treat Vision framework availability carefully because iOS version is not known yet. OCR should begin with still frames and saved images.

## QR and Barcode

QR and barcode scanning are realistic offline features through native camera capture and compatible scanning libraries. These should be prioritized before heavier object detection.

## Document Utilities

Document edge detection, color sampling, brightness estimate, crop, rotate, freeze frame, and contrast enhancement are practical offline tools.

## Inspection Mode

Inspection mode combines detected objects, OCR text, barcode results, sensor state, timestamp, and local rules. It should state uncertainty clearly and save observations locally.
