# Installation and first run — V6.1

1. Open the [GitHub Releases page](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases) and confirm the intended release tag and asset filename.
2. Download the executable or package from that release. The executable itself is not tracked in this source repository.
3. Verify SHA-256 when a digest for the exact same file is published.
4. Install the appropriate OEM USB/ADB driver using a trusted package. Connect the device in the mode required by the chosen workflow.
5. Confirm the phone model/codename/region, firmware package and bootloader state. Back up all data before any destructive operation.
6. Follow [`INSTRUCTIONS.txt`](../INSTRUCTIONS.txt) for AOSP/Custom ROM, HyperOS/MIUI MiFlash, Kernel & Recovery, driver verification and troubleshooting.

## First-run stop conditions

- The detected device or mode does not match the intended workflow.
- The package's model/codename/region cannot be confirmed.
- Partition selection disagrees with trusted ROM instructions.
- A driver/tool check fails or the console reports command errors.
- A script unexpectedly proposes wiping user data or locking the bootloader.

Do not bypass Windows security warnings solely because the file is distributed as an EXE. Verify its origin and digest first.
