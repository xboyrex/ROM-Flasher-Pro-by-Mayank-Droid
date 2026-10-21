# Artifact verification

The release includes `SHA256SUMS.txt`.

Termux:
```bash
sha256sum ROM_Flasher_Pro_V6.exe
```

Windows PowerShell:
```powershell
Get-FileHash .\\ROM_Flasher_Pro_V6.exe -Algorithm SHA256
```

The calculated digest must exactly match the EXE entry in `SHA256SUMS.txt`. A matching hash confirms file integrity against that manifest; it does not independently prove that the program is safe or authentic.
