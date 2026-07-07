# Offline Vision v0.5 XR

The iPhone XR target improves the practical vision path compared with iPhone 6, but no model is claimed to run until device testing proves it.

## Strategy

- Still-image detection first.
- Low-FPS live detection later.
- Use Vision and Core ML where public APIs allow.
- Keep YOLO nano or small model exports as the first object detection path.
- Convert through a Core ML export pipeline once the build environment is chosen.
- Keep QR and barcode scanning separate from heavy object detection.
- Use document edge detection and image utilities before attempting large multimodal models.

## Expected Targets

- Model size: prefer under 25 MB for first tests.
- Still-image latency: under 1500 ms desired, under 3000 ms acceptable for early prototype.
- Live detection: only after still capture is stable.
- OCR: native Vision text recognition or a small local OCR route if compatible with the deployment target.

## Can Test On Windows Now

- Capability routing.
- Adapter result shape.
- Model conversion research notes.
- Mock vision responses.
- XR capability matrix classification.

## Requires iPhone XR

- Camera capture latency.
- Vision/Core ML compatibility.
- Thermal and battery behavior.
- Real OCR quality.
- Real object detection latency.

## Avoid

- Claiming large vision-language model support.
- Cloud vision dependency as the core.
- Building a web camera UI.
