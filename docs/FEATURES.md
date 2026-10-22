# Feature guide — interface-grounded

This guide describes the controls visible in the supplied screenshots. It does not certify the underlying executable's implementation or success behavior.

## AOSP / Custom ROM

Visible controls include a firmware ZIP/IMG selector, a Fastboot partition checklist (`boot`, `init_boot`, `vendor_boot`, `dtbo`, `recovery`, `vbmeta`), an Auto Flash entry point and Fastboot/reboot commands. Select partitions only when trusted instructions for the exact device require them.

## Xiaomi HyperOS / MIUI

Visible controls include a Fastboot ROM archive/folder selector or Recovery ZIP selector, ARB Guard and script modes:
- **Clean All** — labelled as wiping userdata and storage.
- **Save User Data** — intended to preserve user data, but it cannot guarantee preservation.
- **Clean All & Lock Bootloader** — potentially unsafe if the installed firmware does not match the exact device and region. Do not relock based on guesswork.

Check anti-rollback requirements and vendor/device-specific instructions.

## Kernel & Recovery

The dialog shows ZIP/IMG selection and target partitions including `boot`, `recovery`, `init_boot`, `vendor_boot` and `dtbo`. Never choose a target from the filename alone.

## Terminal and device status

The screenshots show app-reported log output, a Clear control, a Refresh control, battery/slot fields and a workflow progress ring. Unknown fields are not proof of valid state. Console output and progress UI should not replace independent verification.

## RAM Cleaner / Windows Memory Cleaner

The Windows dialog screenshot shows used/free physical RAM, a progress bar, selected memory areas and an Optimize Memory Now control. Visible areas include Combined Page List, Modified File Cache, Modified Page List, Registry Cache, Standby List, Low Priority Standby List, System File Cache and Working Set. The exact native API calls and outcomes are not verified by the screenshots. Save work first; benefits depend on system state and may be temporary.

## Official Links

A dialog screenshot shows shortcuts for Mayank Droid Hub, Xiaomi / POCO Mi Unlock, Onyx Services, Otaku Hub Pro and Telegram destinations. Verify destinations before signing in or downloading files.

## Operational safety

Flashing, partition erasing, data wiping and bootloader changes may result in data loss or an unbootable device. Back up data and follow trusted instructions for the exact device and firmware package.
