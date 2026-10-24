``markdown
<!-- ════════════════════════════════════════════════════════════════════════ -->
<!--  ROM FLASHER PRO · V6.1.0 · MAYANK DROID · CYBERPUNK EDITION          -->
<!-- ════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00E5FF,50:7B2FF7,100:9D00FF&height=220&section=header&text=ROM%20FLASHER%20PRO&fontSize=72&fontColor=ffffff&fontAlignY=34&desc=V6.1.0%20%E2%80%94%20CYBERPUNK%20EDITION&descAlignY=58&descSize=16&animation=twinkling&stroke=00E5FF&strokeWidth=2" alt="ROM Flasher Pro" />
</a>

<a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=900&color=00E5FF&center=true&vCenter=true&multiline=true&repeat=true&width=900&height=90&lines=Android+Servicing+Toolkit+for+Windows;AOSP+%C2%B7+HyperOS+%C2%B7+MiFlash+%C2%B7+Kernel+%C2%B7+Recovery;Fastboot+%2B+ADB+Sideload+%2B+EDL+9008" alt="Typing SVG" />
</a>

<p>
  <a href="VERSION"><img src="https://img.shields.io/badge/version-6.1.0-00E5FF?style=for-the-badge&logo=semanticrelease&logoColor=white&labelColor=0D1117" /></a>
  <a href="https://www.microsoft.com/windows"><img src="https://img.shields.io/badge/platform-Windows%2010%2F11%20x64-0078D4?style=for-the-badge&logo=windows&logoColor=white&labelColor=0D1117" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117" /></a>
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/license-see%20SECURITY.md-9D00FF?style=for-the-badge&logo=opensourceinitiative&logoColor=white&labelColor=0D1117" /></a>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/stargazers"><img src="https://img.shields.io/github/stars/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid?style=for-the-badge&logo=github&color=FFD700&labelColor=0D1117" /></a>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases"><img src="https://img.shields.io/github/v/release/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid?style=for-the-badge&logo=github&color=00E5FF&labelColor=0D1117&sort=semver" /></a>
</p>

<p>
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases"><img src="https://cdn.simpleicons.org/github/00E5FF" width="16" /> <b>Latest Release</b></a>
  &nbsp;·&nbsp;
  <a href="CHANGELOG.md"><img src="https://cdn.simpleicons.org/readthedocs/00E5FF" width="16" /> <b>Changelog</b></a>
  &nbsp;·&nbsp;
  <a href="INSTRUCTIONS.txt"><img src="https://cdn.simpleicons.org/gitbook/00E5FF" width="16" /> <b>Flashing Guide</b></a>
  &nbsp;·&nbsp;
  <a href="website/"><img src="https://cdn.simpleicons.org/googlechrome/00E5FF" width="16" /> <b>Website</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/issues"><img src="https://cdn.simpleicons.org/git/FF3B30" width="16" /> <b>Report Bug</b></a>
</p>

<p>
  <img src="https://cdn.simpleicons.org/shieldsdotio/FF3B30" width="16" />
  <b>VERIFY THE PACKAGE · CONFIRM THE DEVICE · REVIEW EACH DESTRUCTIVE ACTION</b>
</p>

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/gitbook/00E5FF" width="24" align="center" /> Overview

**ROM Flasher Pro** is a Windows-facing Android servicing toolkit that unifies fastboot flashing, MiFlash/HyperOS workflows, kernel/recovery image selection, ADB/Fastboot diagnostics, WHQL driver installation and Windows memory optimization into a single, safe, Bento-styled interface.

Designed for Android modders, ROM testers and power users who need a repeatable, verifiable flashing pipeline — with explicit destructive-action guards, on-screen device identity checks and a clean read-only console.

> <img src="https://cdn.simpleicons.org/readthedocs/F9AB00" width="16" /> **Note:** This repository contains documentation, screenshots, visual assets, the static website, release metadata, tests and publishing helpers. The original application source tree is not tracked here. Hotfix notes are consolidated from the supplied build log and are **not** a substitute for an independent source audit or device-specific validation.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

<div align="center">

<table>
<tr>
<td align="center" width="25%">
  <img src="https://cdn.simpleicons.org/android/3DDC84" width="36" /><br/>
  <b>AOSP &amp; Custom ROM</b><br/>
  <sub>payload.bin auto-detect</sub>
</td>
<td align="center" width="25%">
  <img src="https://cdn.simpleicons.org/xiaomi/FF6900" width="36" /><br/>
  <b>HyperOS / MiFlash</b><br/>
  <sub>4 official modes</sub>
</td>
<td align="center" width="25%">
  <img src="https://cdn.simpleicons.org/linux/FFD700" width="36" /><br/>
  <b>Kernel &amp; Recovery</b><br/>
  <sub>AnyKernel3 + IMG</sub>
</td>
<td align="center" width="25%">
  <img src="https://cdn.simpleicons.org/microsoftwindows/0078D4" width="36" /><br/>
  <b>RAM Cleaner</b><br/>
  <sub>10 optimization areas</sub>
</td>
</tr>
</table>

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/git/00E5FF" width="24" align="center" /> V6.1.0 Hotfix Highlights

| Area | Change |
|:---|:---|
| <img src="https://cdn.simpleicons.org/figma/00E5FF" width="16" /> UI Stability | Reduced redundant redraws, more stable panel geometry, cleaner tab repainting, on-demand progress animation |
| <img src="https://cdn.simpleicons.org/android/3DDC84" width="16" /> Device Detection | Clearer ADB/Fastboot state handling, explicit refresh, connection checks before device-dependent actions |
| <img src="https://cdn.simpleicons.org/readthedocs/9D00FF" width="16" /> Package Routing | Auto-detect `.zip` / `.tgz` / `.img`, payload-based AOSP detection, HyperOS/MIUI workflow auto-selection |
| <img src="https://cdn.simpleicons.org/apachekafka/FF6900" width="16" /> Large Sideload | Chunked transfer path for large ROM ZIPs, cleaner ADB environment, less extraction noise |
| <img src="https://cdn.simpleicons.org/wrench/00E5FF" width="16" /> Driver Workflow | Consolidated driver panel with console verification of bundled tools and 5 WHQL driver groups |
| <img src="https://cdn.simpleicons.org/gnometerminal/3DDC84" width="16" /> Console Quality | Read-only log output, clearer line separation, better wrapping, duplicate prefix removal |
| <img src="https://cdn.simpleicons.org/memcached/9D00FF" width="16" /> RAM Cleaner | Ten memory-optimization stages including heap/GC cleanup and temp/USB buffer purge |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/github/00E5FF" width="24" align="center" /> Interface Gallery

<div align="center">

<table>
<tr>
<td align="center" width="33%">
  <img src="1.png" width="100%" alt="AOSP & Custom ROM" /><br/>
  <sub><b>01</b> · AOSP &amp; Custom ROM</sub>
</td>
<td align="center" width="33%">
  <img src="2.png" width="100%" alt="HyperOS & MiFlash" /><br/>
  <sub><b>02</b> · HyperOS &amp; MIUI MiFlash</sub>
</td>
<td align="center" width="33%">
  <img src="3.png" width="100%" alt="Kernel & Recovery" /><br/>
  <sub><b>03</b> · Kernel &amp; Recovery</sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
  <img src="4.png" width="100%" alt="Terminal Console" /><br/>
  <sub><b>04</b> · Terminal Console (Idle)</sub>
</td>
<td align="center" width="33%">
  <img src="5.png" width="100%" alt="MiFlash Driver Installer" /><br/>
  <sub><b>05</b> · MiFlash Driver Installer</sub>
</td>
<td align="center" width="33%">
  <img src="6.png" width="100%" alt="Tool Verification" /><br/>
  <sub><b>06</b> · Tool Verification Console</sub>
</td>
</tr>
<tr>
<td align="center" width="33%">
  <img src="7.png" width="100%" alt="Official Links" /><br/>
  <sub><b>07</b> · Mayank Droid Official Links</sub>
</td>
<td align="center" width="33%">
  <img src="8.png" width="100%" alt="RAM Cleaner" /><br/>
  <sub><b>08</b> · RAM Cleaner</sub>
</td>
<td align="center" width="33%">
  <img src="https://cdn.simpleicons.org/github/0D1117" width="40" /><br/>
  <sub>More in <a href="screenshots/v6.1/">screenshots/v6.1/</a></sub>
</td>
</tr>
</table>

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/task/00E5FF" width="24" align="center" /> Functional Areas

| Area | Workflow | Review Before Use |
|:---|:---|:---|
| <img src="https://cdn.simpleicons.org/android/3DDC84" width="16" /> AOSP / Custom ROM | ZIP/IMG selection, payload partition list, Fastboot controls, Auto Flash | Confirm device codename, package integrity, required partitions |
| <img src="https://cdn.simpleicons.org/xiaomi/FF6900" width="16" /> HyperOS / MIUI MiFlash | Fastboot package or Recovery ZIP, script modes, ARB Guard | Confirm region/build and anti-rollback constraints. Clean All erases data; Clean All &amp; Lock can brick a mismatched device |
| <img src="https://cdn.simpleicons.org/linux/FFD700" width="16" /> Kernel &amp; Recovery | Select image + target partition | Never infer destination partition from a filename alone |
| <img src="https://cdn.simpleicons.org/gnometerminal/00E5FF" width="16" /> ADB / Fastboot Console | Device state, console output, refresh, reboot | Verify connection state independently; console text is not proof of a successful flash |
| <img src="https://cdn.simpleicons.org/wrench/9D00FF" width="16" /> Drivers &amp; Bundled Tools | Driver installation and console verification | Install only trusted, compatible drivers and check results |
| <img src="https://cdn.simpleicons.org/memcached/3DDC84" width="16" /> RAM Cleaner | Memory display + optimization controls | Save work first. Cache cleanup may have temporary effects |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/rocket/00E5FF" width="24" align="center" /> Installation &amp; First Run

<div align="center">
<table>
<tr>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/github/00E5FF" width="32" /><br/><b>1</b><br/><sub>Open Releases</sub></td>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/downloads/9D00FF" width="32" /><br/><b>2</b><br/><sub>Download</sub></td>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/shieldsdotio/3DDC84" width="32" /><br/><b>3</b><br/><sub>Verify SHA-256</sub></td>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/wrench/FFD700" width="32" /><br/><b>4</b><br/><sub>Install Drivers</sub></td>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/android/3DDC84" width="32" /><br/><b>5</b><br/><sub>Confirm Device</sub></td>
<td align="center" width="16%"><img src="https://cdn.simpleicons.org/readthedocs/FF6900" width="32" /><br/><b>6</b><br/><sub>Follow Guide</sub></td>
</tr>
</table>
</div>

1. **Open** the [GitHub Releases](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases) page and confirm the version and exact asset name.
2. **Download** the executable from the intended release. *The executable is not tracked in this repository's source tree.*
3. **Verify** the SHA-256 digest when a matching digest is published for that exact asset:
   ```powershell
   Get-FileHash .\ROM_Flasher_Pro_By_Mayank_Droid.exe -Algorithm SHA256
   ```
4. **Install** the appropriate OEM/ADB USB driver. Connect the phone in the mode required by the selected workflow.
5. **Confirm** model, codename, region, bootloader state and firmware source **before** starting any flash operation.
6. **Follow** the [V6.1 instructions](INSTRUCTIONS.txt). Stop if the application status, partition list or device identity conflicts with trusted device-specific instructions.

### Launchers

| File | Purpose |
|:---|:---|
| `ADB_Toolkit_V6.exe` | Primary launcher (Admin UAC manifest included) |
| `ROM_Flasher_Pro_By_Mayank_Droid.exe` | Alternate packaged launcher |
| `run.bat` | Source-run launcher |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/shieldsdotio/FF3B30" width="24" align="center" /> Safety &amp; Scope

Flashing, partition erasure, data formatting and bootloader changes **can cause irreversible data loss or leave a device unbootable**.

**Before you flash:**

- <img src="https://cdn.simpleicons.org/checkmarx/3DDC84" width="16" /> Back up all important data and confirm the exact device model/codename.
- <img src="https://cdn.simpleicons.org/checkmarx/3DDC84" width="16" /> Verify firmware provenance, package integrity and intended partition list.
- <img src="https://cdn.simpleicons.org/checkmarx/3DDC84" width="16" /> Treat `Format Data`, `Erase Userdata`, `Clean All` and bootloader relocking as potentially destructive.
- <img src="https://cdn.simpleicons.org/checkmarx/3DDC84" width="16" /> Stop immediately if device detection, selected workflow or on-screen status conflicts with trusted device-specific instructions.

**Do not:**

- <img src="https://cdn.simpleicons.org/x/FF3B30" width="16" /> Select **Clean All &amp; Lock** unless trusted, device-specific release instructions explicitly permit relocking with that exact firmware.
- <img src="https://cdn.simpleicons.org/x/FF3B30" width="16" /> Use EDL/9008 flows outside an authorized and device-appropriate process.
- <img src="https://cdn.simpleicons.org/x/FF3B30" width="16" /> Interrupt a flash or EDL session — it can permanently brick the device.
- <img src="https://cdn.simpleicons.org/x/FF3B30" width="16" /> Run other ADB/Fastboot tools simultaneously with this toolkit.

> <img src="https://cdn.simpleicons.org/shieldsdotio/FF3B30" width="16" /> The repository's screenshots show the user interface, not the application's source code or an assurance that each operation is safe on every model. Use device-specific maintainer instructions and independently verify the resulting device state.

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/checkmarx/3DDC84" width="24" align="center" /> Validation &amp; QA

<p>
  <img src="https://img.shields.io/badge/py__compile-0%20warnings-3DDC84?style=for-the-badge&logo=python&logoColor=white&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/runtime--init-verified-3DDC84?style=for-the-badge&logo=checkmarx&logoColor=white&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/ADB%20polling-no%20subprocess-00E5FF?style=for-the-badge&logo=android&logoColor=white&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/sideload-64%20KB%20chunks-9D00FF?style=for-the-badge&logo=apachekafka&logoColor=white&labelColor=0D1117" />
  <img src="https://img.shields.io/badge/detection-~0.25s-FFD700?style=for-the-badge&logo=speedtest&logoColor=white&labelColor=0D1117" />
</p>

- `python3 -W error -m py_compile` — **0 warnings** across all 8 Python modules
- Runtime init verified with `ROMFlasherProApp()`
- ADB state polling verified without subprocess spawning
- Large-sideload path verified with 64 KB chunked streaming
- Device detection latency ≈ **0.25 s** for Sideload/Fastboot states
- Duplicate EXEs and unused icons removed from release package
- MiFlash driver/tool verification list confirmed in Terminal Console

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/github/00E5FF" width="24" align="center" /> Release Artifacts

| Asset | Description |
|:---|:---|
| <img src="https://cdn.simpleicons.org/github/00E5FF" width="16" /> [Latest Release](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases/latest) | Current downloadable build |
| <img src="https://cdn.simpleicons.org/git/9D00FF" width="16" /> [All Releases](https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid/releases) | Full release history |
| <img src="https://cdn.simpleicons.org/readthedocs/00E5FF" width="16" /> [CHANGELOG.md](CHANGELOG.md) / [CHANGELOG.txt](CHANGELOG.txt) | Detailed change record |
| <img src="https://cdn.simpleicons.org/gitbook/FF6900" width="16" /> [INSTRUCTIONS.txt](INSTRUCTIONS.txt) | Workflow-specific operating guide |
| <img src="https://cdn.simpleicons.org/readthedocs/3DDC84" width="16" /> [RELEASE_NOTES.md](RELEASE_NOTES.md) | Release summary |
| <img src="https://cdn.simpleicons.org/shieldsdotio/FFD700" width="16" /> [ROM_Flasher_Pro_By_Mayank_Droid.exe.sha256](ROM_Flasher_Pro_By_Mayank_Droid.exe.sha256) | Package integrity digest |

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/readthedocs/00E5FF" width="24" align="center" /> Repository Map

```text
ROM-Flasher-Pro-by-Mayank-Droid/
├── assets/                  # SVG icons & branding
├── docs/                    # Documentation & guides
├── screenshots/v6.1/        # V6.1 interface screenshots
├── scripts/                 # Build & publishing helpers
├── tests/                   # Validation tests
├── website/                 # Static project website
├── 1.png … 8.png            # Root-level gallery assets
├── CHANGELOG.md / .txt      # Change records
├── INSTRUCTIONS.txt         # Flashing guide
├── README.md                # This file
├── RELEASE_NOTES.md         # Release summary
├── SECURITY.md              # Security policy
├── SUPPORT.md               # Support channels
├── VERSION                  # Current version
└── .gitignore
```

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/codepen/00E5FF" width="24" align="center" /> Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,html,css,js,bash,windows,git,github,vscode&theme=dark&perline=9" alt="Tech Stack" />

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/github/00E5FF" width="24" align="center" /> GitHub Stats

<div align="center">

<img height="170em" src="https://github-readme-stats.vercel.app/api?username=xboyrex&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&icon_color=9D00FF&text_color=FFFFFF&include_all_commits=true&count_private=true" />
<img height="170em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=xboyrex&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&text_color=FFFFFF&langs_count=8" />

<br/><br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=xboyrex&theme=tokyonight&hide_border=true&background=0D1117&ring=00E5FF&fire=9D00FF&currStreakLabel=00E5FF" />

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=xboyrex&theme=tokyonight&no-frame=true&no-bg=true&column=7&margin-w=15&margin-h=15" />

</div>

<div align="center">

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=xboyrex&theme=tokyo-night&bg_color=0D1117&color=00E5FF&line=9D00FF&point=FFFFFF&area=true&hide_border=true" alt="Activity Graph" />

</div>

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="" />

## <img src="https://cdn.simpleicons.org/githubspo
