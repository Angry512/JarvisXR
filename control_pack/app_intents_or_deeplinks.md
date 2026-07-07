# App Intents Or Deep Links

The most reliable bridge is the URL scheme:

- `jarvis://command?text=help`
- `jarvis://command?text=system%20check`
- `jarvis://command?text=inspect%20mode`
- `jarvis://command?text=quiet%20mode`
- `jarvis://command?text=normal%20mode`
- `jarvis://command?text=voice%20test`
- `jarvis://inspect`
- `jarvis://diagnostics`
- `jarvis://settings`
- `jarvis://standby`
- `jarvis://online`

App Intent source files are included in the app project for:

- Run JARVIS Command
- Start JARVIS Inspection
- Set JARVIS Quiet Mode
- Set JARVIS Normal Mode
- Open JARVIS Diagnostics
- Test JARVIS Voice

Because this machine is Windows-only, GitHub Actions with Xcode must verify App Intents compilation. If App Intents fail, keep the URL scheme path. Shortcuts can still call `jarvis://` links.
