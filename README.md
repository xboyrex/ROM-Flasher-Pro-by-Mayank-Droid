<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=8&color=0:00E5FF,48:7457FF,100:0B1020" width="100%" alt="" />

<img src="https://img.shields.io/badge/XBOYREX-MAYANK_DROID-0B1020?style=for-the-badge&labelColor=0B1020&color=00D9FF" alt="XBOYREX Mayank Droid" />

# ROM FLASHER PRO

### V6.0.0 · WINDOWS FLASHING UTILITY

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&duration=2400&pause=700&color=00D9FF&center=true&vCenter=true&width=680&lines=DEVICE+TOOLS.+CLEAR+WORKFLOWS.;VERIFY+FIRST.+FLASH+CAREFULLY.;BUILT+FOR+ANDROID+POWER+USERS." alt="ROM Flasher Pro tagline" />

<p>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest"><img src="https://img.shields.io/github/v/release/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid?style=for-the-badge&label=LATEST%20RELEASE&color=00D9FF&labelColor=0B1020" alt="Latest release" /></a>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases"><img src="https://img.shields.io/badge/PLATFORM-WINDOWS-0B1020?style=for-the-badge&logo=windows&logoColor=00D9FF" alt="Windows" /></a>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid"><img src="https://img.shields.io/badge/RELEASE-BINARY_ONLY-0B1020?style=for-the-badge&logo=github&logoColor=8B5CF6" alt="Binary-only release" /></a>
</p>

<p>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest">DOWNLOAD LATEST BUILD</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/issues">REPORT AN ISSUE</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/xboyrex">DEVELOPER PROFILE</a>
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:00E5FF,48:7457FF,100:0B1020" width="100%" alt="" />

</div>

## 01 / Overview

**ROM Flasher Pro** is a Windows executable for Android device flashing workflows. The V6.0.0 release is distributed as a compiled binary; source code is not included in this repository.

The interface and workflow are designed around device preparation, firmware checks, partition staging, and explicit operator control. Actual compatibility depends on the device, firmware package, bootloader state, and installed platform tools.

> **Important:** Flashing can erase data or make a device unbootable. Confirm the exact device model and firmware, keep a verified backup, and understand the recovery process before proceeding.

## 02 / Capabilities

<table>
  <tr>
    <td width="50%" valign="top">

### <img src="https://img.shields.io/badge/01-00D9FF?style=flat-square&labelColor=0B1020" alt="01" /> Partition workflow

Direct-write workflow is described for `boot`, `init_boot`, `vendor_boot`, and `dtbo`. Only flash partitions supported by your exact device and firmware.

</td>
    <td width="50%" valign="top">

### <img src="https://img.shields.io/badge/02-8B5CF6?style=flat-square&labelColor=0B1020" alt="02" /> Firmware handling

Release notes describe native archive extraction and handling of `flash_all.bat`. Inspect package contents and scripts before execution.

</td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### <img src="https://img.shields.io/badge/03-00D9FF?style=flat-square&labelColor=0B1020" alt="03" /> Verification

Use SHA-256 to check that the downloaded executable matches the published checksum. A matching hash confirms file integrity against that checksum, not that the program is risk-free.

</td>
    <td width="50%" valign="top">

### <img src="https://img.shields.io/badge/04-8B5CF6?style=flat-square&labelColor=0B1020" alt="04" /> Operator control

The project describes a process-termination lock on window closure. Do not close the application or disconnect the device during an active flash operation unless its instructions explicitly say it is safe.

</td>
  </tr>
</table>

## 03 / Interface preview

Screenshots below are loaded from the repository root. Select any image to open the original file.

<div align="center">

| Studio Dashboard | Partition Staging |
|:---:|:---:|
| [![Studio Dashboard](1.png)](1.png) | [![Partition Staging](2.png)](2.png) |
| Firmware Verification | Hardware Console |
| [![Firmware Verification](3.png)](3.png) | [![Hardware Console](4.png)](4.png) |
| Kernel Injection | Flash Workflow |
| [![Kernel Injection](5.png)](5.png) | [![Flash Workflow](6.png)](6.png) |

[![Additional interface screenshot](7.png)](7.png)

</div>

## 04 / Download

<div align="center">

### ROM Flasher Pro V6.0.0

<a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest">
  <img src="https://img.shields.io/badge/DOWNLOAD_FOR_WINDOWS-V6.0.0-00D9FF?style=for-the-badge&logo=windows&logoColor=0B1020&labelColor=0B1020" alt="Download ROM Flasher Pro for Windows" />
</a>

**[Open latest release and verify its assets](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest)**

</div>

### Download from PowerShell

Open PowerShell and run:

```powershell
$uri = "https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest/download/ROM_Flasher_Pro_V6.exe"
Invoke-WebRequest -Uri $uri -OutFile ".\ROM_Flasher_Pro_V6.exe"
```

If the asset name changes in a future release, download the executable directly from the release page instead.

## 05 / Verify the download

In PowerShell, run:

```powershell
Get-FileHash .\ROM_Flasher_Pro_V6.exe -Algorithm SHA256
```

The checksum recorded in the repository's release information is:

```text
2834E7E3D84819EFE4238D3018CFECCA710B3801A6295177972716A27FA7979E
```

Compare the entire output hash with the checksum published for the **same release asset**. If they differ, do not run the file; download it again from the official release page and re-check. If the release asset or checksum has changed, trust the checksum published for the current release, not an old README value.

## 06 / Requirements and workflow

1. Use a supported Windows PC and install Android Platform Tools (`adb` and `fastboot`) from an official source.
2. Install the correct USB driver for your device when required.
3. Back up important data. Confirm the exact device model, firmware region/build, bootloader state, and partition layout.
4. Charge the device and use a reliable USB cable and direct USB port.
5. Follow the instructions supplied with the release. Do not flash files intended for a different device.
6. Keep the device connected while an operation is active. Do not interrupt flashing or power off the PC during writes.
7. Verify the final device state before disconnecting.

Example: reboot a connected Android device into bootloader mode:

```powershell
adb devices
adb reboot bootloader
fastboot devices
```

Run these commands only when appropriate for your device. A device shown by `adb` may disappear from ADB and reappear under Fastboot; that is expected on many devices.

## 07 / Safety notes

- Unlocking a bootloader commonly wipes user data and may affect device security or warranty.
- Never flash `boot`, `init_boot`, `vendor_boot`, `dtbo`, or other partitions solely because the option is visible. Confirm compatibility first.
- Do not use firmware from another model or variant.
- Keep a backup and a recovery plan available before modifying partitions.
- Run downloaded executables only if you trust the source and have independently checked the release information. SHA-256 is an integrity check, not a malware scan.
- This project is provided as-is. Use it at your own risk.

## 08 / Support and release history

- **Latest release:** [V6.0.0 and assets](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest)
- **All releases:** [Release history](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases)
- **Issues:** [Report a bug or compatibility problem](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/issues)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)
- **Release notes:** [RELEASE_NOTES.md](RELEASE_NOTES.md)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&height=3&color=0:00E5FF,48:7457FF,100:0B1020" width="100%" alt="" />

**XBOYREX / MAYANK DROID**

<sub>ANDROID TOOLS · VERIFY BEFORE FLASHING · DOCUMENT EVERY RELEASE</sub>

</div>
