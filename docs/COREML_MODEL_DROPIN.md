# Core ML Model Drop-In

JARVIS can detect whether a compiled Core ML model is bundled, but this repo does not currently include one.

## Current Real Vision Features

- Camera preview through AVFoundation.
- Photo capture.
- Apple Vision text recognition after capture.
- Apple Vision barcode and QR detection after capture.
- Image size and capture metadata summary.

## Object Detection Status

YOLO-style or general object detection is prepared but not active. Add a compiled model to:

`ios/JarvisXR/JarvisXR/Models/`

Supported checked names:

- `JarvisObjectDetector.mlmodelc`
- `YOLO.mlmodelc`
- `YOLOv8n.mlmodelc`
- `ObjectDetector.mlmodelc`

After adding a model, include it in the XcodeGen project sources and rebuild through GitHub Actions. Do not claim object detection works until the model is bundled, called through Vision, installed on the phone, and tested on the iPhone.
