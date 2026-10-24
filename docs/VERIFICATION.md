# Artifact verification

A checksum is meaningful only when it is compared with the digest published for the **same exact artifact**.

## Windows PowerShell

```powershell
Get-FileHash .\ADB_Toolkit_V6.exe -Algorithm SHA256
```

## Termux / Linux

```bash
sha256sum ADB_Toolkit_V6.exe
```

The currently observed GitHub asset `ADB_Toolkit_V6.exe` has the SHA-256 digest below in the existing `v6.0.0` release metadata:

```text
f122777f1c99be529b4293defedafe34153744f698c11a87aa2937ea6c28437d  ADB_Toolkit_V6.exe
```

Use this value only for the exact binary whose release metadata publishes that digest. If the executable changes, recalculate the hash. When a new V6.1.0 release is created, verify the digest against the file uploaded to that release.

A matching digest confirms byte-for-byte equality with the expected file; it does not independently establish software safety, authorship or malware-free status.
