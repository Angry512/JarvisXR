# JARVIS Visual System

This is the visual rule set for the installable native app and the Windows preview.

## Identity

- Visible product name: `JARVIS`
- Do not show `XR` in product UI.
- The interface should feel like a full-screen dedicated AI instrument, not a terminal, website, dashboard, or small preview inside the phone.

## Colors

- Background: near black.
- Panels: layered black graphite with subtle borders.
- Primary accent: cyan.
- Secondary accent: cool green for voice or ready states.
- Warning accent: muted amber for quiet or confirmation states.
- Error accent: restrained red only for refusal or failure states.

## Orb

- Idle: slow cyan pulse.
- Listening: brighter inbound pulse and clear Listening label.
- Processing: rotating scan sweep.
- Speaking: green outbound pulse and clear Speaking label.
- Quiet: dimmer amber or reduced cyan energy.
- Inspection: sharper scan ring and cooler cyan highlight.
- Blocked: restrained amber or red accent.

The orb is drawn natively in Swift/UIKit and tkinter. The generated reference image is only a source for visual direction and asset readiness.

## Panels And Controls

- Panels should have dark depth, thin borders, and readable text.
- Buttons should feel like controls, not links.
- Command input should be obvious and polished.
- Recent Activity is not shown on the main screen.
- Text responses are brief and transient on the home screen. Long results belong in secondary screens or command-specific views.

## Voice Tone

- Natural by default.
- Friendly is available for warmer output.
- Crisp for faster command feedback.
- Quiet for lower volume and slower delivery.
- Profile preview is available in Settings.
- Personal Voice can be requested through public iOS authorization where supported. It is not trained, cloned, uploaded, or guaranteed.
- No cloud voice and no paid voice dependency.

## Avoid

- Web UI.
- Terminal-first layout.
- Childish sci-fi styling.
- Fake system control claims.
- Raw rectangular reference image as the app icon.
