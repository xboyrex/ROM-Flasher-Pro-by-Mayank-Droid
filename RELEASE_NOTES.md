# ROM Flasher Pro V6.1.0 — Hotfix Release Notes

## Application changes reported for this build

- Stabilized device-status rendering and reduced redundant idle UI updates.
- Improved ADB/Fastboot status handling, explicit refresh behavior and device-dependent action checks.
- Added payload-aware partition discovery and smarter routing for supported AOSP ZIP, HyperOS/MIUI TGZ, kernel ZIP and IMG inputs.
- Added a chunked sideload path for large ROM archives and cleaner extraction/terminal output.
- Improved terminal read-only behavior, line separation, wrapping and status-message consistency.
- Added driver-installation and bundled-tool verification panels.
- Expanded the reported RAM Cleaner workflow to ten memory-optimization stages.
- Corrected the reported Python warning and startup initialization issues.

The detailed list and evidence boundaries are recorded in [`CHANGELOG.txt`](CHANGELOG.txt).

## User documentation

- [`INSTRUCTIONS.txt`](INSTRUCTIONS.txt) — AOSP / Custom ROM, HyperOS / MIUI MiFlash, Kernel & Recovery, diagnostics, drivers and troubleshooting.
- [`docs/FEATURES.md`](docs/FEATURES.md) — interface-grounded feature inventory.
- [`docs/VERIFICATION.md`](docs/VERIFICATION.md) — exact-file SHA-256 verification.

## Release artifact note

The existing GitHub release asset is named `ADB_Toolkit_V6.exe` and is currently attached to the `v6.0.0` release page. To make V6.1.0 a standalone release, publish the `v6.1.0` tag/release and attach the intended executable to that release; a binary asset attached to one release does not automatically become an asset of another release.

The repository contains documentation, screenshots, visual assets, a static website and release metadata—not the original application source tree. These notes describe the supplied build report and do not constitute an independent source audit or a guarantee of behavior on every device.
