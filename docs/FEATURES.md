# Feature guide — V6.1 interface and supplied build notes

This guide describes the visible interface plus the behaviors reported in the supplied build notes. A screenshot can establish what a control looks like, but does not certify the implementation or successful results on every device.

## AOSP / Custom ROM

The workspace shows firmware ZIP/IMG selection, a Fastboot partition checklist, Auto Flash entry point and reboot/erase controls. Supplied notes describe payload.bin header inspection and automatic detection of supported boot-related partitions. Confirm the exact codename and use only the partitions prescribed by the ROM maintainer.

## Xiaomi HyperOS / MIUI MiFlash

The workspace shows a Fastboot ROM archive/folder or Recovery ZIP selector, script modes, ARB Guard and driver/tool verification. The supplied notes report routing logic for supported `.tgz` Fastboot packages and AOSP payload ZIPs accidentally selected from this area.

- **Clean All:** destructive; expects user data to be erased.
- **Save User Data:** intended to preserve user data but cannot guarantee preservation.
- **Clean All & Lock Bootloader:** high risk. Do not use unless exact model/region firmware and trusted maintainer instructions explicitly permit relocking.
- **EDL / 9008:** only for an authorized, device-appropriate service process.

## Kernel & Recovery

The dialog shows ZIP/IMG selection and target partitions such as `boot`, `recovery`, `init_boot`, `vendor_boot` and `dtbo`. These partitions are not interchangeable. Select a target from trusted device-specific instructions, not from the filename alone.

## Terminal and device status

The interface shows console output, a Clear action, Refresh, status indicators and workflow progress. Supplied notes report cleaner read-only log rendering, newline protection, improved text wrapping and a direct ADB-server TCP polling path. Console output and the progress UI should not replace independent verification of a destructive command.

## Driver installation and verification

The new screenshots show a driver panel with individual install controls and an aggregate install/verification action. Supplied notes list Google/Xiaomi WinUSB, Qualcomm QDLoader 9008, Microsoft RNDIS, Microsoft MTP and NVIDIA USB driver groups, plus a console report for the bundled tools. Install only trusted drivers compatible with the connected device and Windows build.

## RAM Cleaner / Windows memory optimization

The existing repository screenshot shows memory usage, selected memory areas and an optimize action. The supplied build notes report ten stages, including CRT heap/GC compaction and temporary/USB-buffer cleanup. The exact native calls and outcomes are not verified by screenshots; effects vary by system, and memory cleanup is not guaranteed to improve responsiveness.

## Official links

A screenshot shows project/community shortcuts. Verify a destination before signing in, downloading files or entering credentials.

## Operational safety

Flashing, partition erasure, data formatting and bootloader changes can cause irreversible data loss or leave a device unbootable. Back up data, verify the firmware/package and follow trusted instructions for the exact device. Never lock the bootloader with incompatible firmware.
