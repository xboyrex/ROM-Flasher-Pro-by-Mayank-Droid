# ROM Flasher Pro V6

**Windows Android-flashing utility | Release: V6.0.0**

ROM Flasher Pro provides a graphical workflow for Android device maintenance tasks involving ADB/Fastboot and supported flashing packages. Always confirm device compatibility and understand each operation before proceeding.

## Download

Get the latest Windows executable and the portable release bundle from the [GitHub Releases page](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases).

- **Windows executable:** `ROM_Flasher_Pro_V6.exe`
- **Portable bundle:** `ROM_Flasher_Pro_V6_Source_and_Release.zip`
- **Integrity:** SHA-256 checksums are included with the release.

## Requirements

- Windows 10/11 (64-bit recommended)
- A compatible USB cable and device-specific USB drivers
- Android Platform Tools / ADB-Fastboot support where required
- Device-specific firmware and a verified package compatible with the exact model

## Safe-use checklist

1. Back up important data before flashing or erasing any partition.
2. Verify the device model, region, firmware build, and partition layout.
3. Use only firmware and images intended for the exact device.
4. Keep the device charged and do not disconnect USB during an active operation.
5. Read each destructive-action confirmation carefully. Factory reset, metadata erasure, and partition flashing can cause data loss or render a device unbootable if used incorrectly.
6. This project does not guarantee compatibility with every Android device or firmware.

## Repository contents

- `docs/` — usage, release, and integrity documentation
- `scripts/` — checksum verification helper
- `VERSION` — release version metadata
- Release assets — compiled Windows executable, portable ZIP, and SHA-256 manifest

## Source-code availability

This repository currently distributes a compiled Windows executable and supporting documentation. The original application source code was not supplied with the EXE, so it is **not represented as source code here**. The portable ZIP is a release bundle, not a claim that the original application source has been reconstructed.

## Verify a download

Compare the SHA-256 value shown on the GitHub Release page with the checksum calculated locally. On Windows PowerShell:

```powershell
Get-FileHash .\\ROM_Flasher_Pro_V6.exe -Algorithm SHA256
```

On Termux/Linux:

```bash
sha256sum ROM_Flasher_Pro_V6.exe
```

## Release

See [Releases](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases) for the current executable and portable bundle.
