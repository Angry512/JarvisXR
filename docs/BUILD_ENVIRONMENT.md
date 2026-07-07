# Build Environment

## Windows Now

Windows can create the repo, run Python tests, validate the registry, run CLI routing, edit docs, prepare mock adapters, and package source artifacts.

Inspection commands before installing anything:

```powershell
python --version
python -m pip --version
git --version
where python
where git
```

## WSL, Linux, or Theos Later

Jailbreak tweak and daemon packaging may require Theos, dpkg tools, and a Unix-like environment. WSL or Raspberry Pi Linux may be enough depending on the target jailbreak and SDK needs.

Inspection commands:

```bash
uname -a
which make
which clang
which dpkg-deb
which theos
```

## Raspberry Pi Later

The Pi can act as dock, backup target, package host, sync server, and recovery station. It should not become the main Jarvis brain.

## Mac Only If Needed

A Mac may be required for certain Xcode, signing, Core ML conversion, or legacy iOS build workflows. Do not assume it is required until the native route and exact iOS version are chosen.

## Tooling Rule

Inspect first, install second. Record versions in build logs.
