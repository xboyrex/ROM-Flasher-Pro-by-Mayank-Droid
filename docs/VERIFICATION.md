# Artifact verification

A checksum is useful only when compared with the expected digest published for the **same exact release artifact**.

## Windows PowerShell

```powershell
Get-FileHash .\ROM_Flasher_Pro_By_Mayank_Droid.exe -Algorithm SHA256
```

## Termux / Linux

```bash
sha256sum ROM_Flasher_Pro_By_Mayank_Droid.exe
```

The tracked checksum file in this repository names `ROM_Flasher_Pro_By_Mayank_Droid.exe`. Check the current release's asset name and checksum manifest before relying on it. If the executable version changes, the digest must change with it.

A matching hash confirms the file matches a supplied digest; it does not independently establish software safety, authorship or malware-free status.
