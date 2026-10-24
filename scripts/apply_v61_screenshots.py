#!/usr/bin/env python3
"""Install the supplied V6.1 screenshot set into a cloned ROM Flasher Pro repository.

Usage from the repository root:
  python apply_v61_screenshots.py /path/to/ROM_Flasher_Pro_V6.1_Screenshots.zip

This copies screenshots only. Review `git diff` before committing or pushing.
"""
from __future__ import annotations
import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path

MAP = {
    "01-aosp-custom-rom.png": {
        "root": "1.png",
        "readme": "docs/readme-screenshots/aosp-custom-rom.png",
        "website": "website/screenshots/1.png",
    },
    "02-hyperos-miui-miflash.png": {
        "root": "2.png",
        "readme": "docs/readme-screenshots/hyperos-miui.png",
        "website": "website/screenshots/4.png",
    },
    "03-kernel-recovery.png": {
        "root": "3.png",
        "readme": "docs/readme-screenshots/kernel-recovery.png",
        "website": "website/screenshots/5.png",
    },
    "04-terminal-console-idle.png": {
        "root": "6.png",
        "readme": "docs/readme-screenshots/terminal-console-idle.png",
        "website": "website/screenshots/9.png",
    },
    "05-driver-installation.png": {
        "root": "5.png",
        "readme": "docs/readme-screenshots/driver-installation.png",
        "website": "website/screenshots/8.png",
    },
    "06-tool-verification-console.png": {
        "root": "4.png",
        "readme": "docs/readme-screenshots/terminal-console.png",
        "website": "website/screenshots/6.png",
    },
    "07-official-links.png": {
        "root": "7.png",
        "readme": "docs/readme-screenshots/official-links.png",
        "website": "website/screenshots/7.png",
    },
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path, help="Path to ROM_Flasher_Pro_V6.1_Screenshots.zip")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root (default: current directory)")
    args = parser.parse_args()
    repo = args.repo.resolve()
    archive = args.archive.resolve()
    if not (repo / ".git").exists():
        raise SystemExit(f"Not a Git repository: {repo}")
    if not archive.is_file():
        raise SystemExit(f"Screenshot archive not found: {archive}")

    with tempfile.TemporaryDirectory(prefix="romflasher-v61-") as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(tmp_path)
        src_dir = tmp_path / "ROM_Flasher_Pro_V6.1_Screenshots"
        missing = [name for name in MAP if not (src_dir / name).is_file()]
        if missing:
            raise SystemExit("Screenshot archive is missing: " + ", ".join(missing))
        stale_checksum = repo / "ROM_Flasher_Pro_By_Mayank_Droid.exe.sha256"
        if stale_checksum.exists():
            stale_checksum.unlink()
        count = 0
        for name, targets in MAP.items():
            src = src_dir / name
            for relative in targets.values():
                dest = repo / relative
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                count += 1
        # Keep a semantic screenshot set in the repository for maintainers and direct downloads.
        semantic_dir = repo / "screenshots" / "v6.1"
        semantic_dir.mkdir(parents=True, exist_ok=True)
        for name in MAP:
            shutil.copy2(src_dir / name, semantic_dir / name)
        for extra in ("README.txt", "SHA256SUMS.txt"):
            if (src_dir / extra).is_file():
                shutil.copy2(src_dir / extra, semantic_dir / extra)

        # Extend the static website gallery only if the V6.1 cards are not already present.
        index = repo / "website" / "index.html"
        if index.is_file():
            html = index.read_text(encoding="utf-8")
            html = html.replace('All screens <span>07</span>', 'All screens <span>09</span>')
            html = html.replace('System tools <span>02</span>', 'System tools <span>03</span>')
            html = html.replace('Console &amp; links <span>02</span>', 'Console &amp; links <span>03</span>')
            html = html.replace('Showing 7 screenshots', 'Showing 9 screenshots')
            marker = '          <figure class="gallery-card" data-category="system"><button type="button" data-lightbox="./screenshots/2.png" aria-label="Open additional app screenshot"><img loading="lazy" src="./screenshots/2.png" alt="Additional ROM Flasher Pro application view"><span class="image-open">↗</span></button><figcaption><span>07 / OVERVIEW</span><strong>Application overview</strong><p>Device status, progress and navigation structure.</p></figcaption></figure>'
            additions = marker + '\n' + \
                '          <figure class="gallery-card" data-category="system"><button type="button" data-lightbox="./screenshots/8.png" aria-label="Open driver installation screenshot"><img loading="lazy" src="./screenshots/8.png" alt="Driver installation panel"><span class="image-open">↗</span></button><figcaption><span>08 / DRIVERS</span><strong>Driver Installation</strong><p>Driver groups with individual and combined controls.</p></figcaption></figure>\n' + \
                '          <figure class="gallery-card" data-category="console"><button type="button" data-lightbox="./screenshots/9.png" aria-label="Open idle terminal workspace screenshot"><img loading="lazy" src="./screenshots/9.png" alt="Idle terminal console workspace"><span class="image-open">↗</span></button><figcaption><span>09 / CONSOLE</span><strong>Console Workspace</strong><p>Terminal layout before command output is populated.</p></figcaption></figure>'
            if 'data-lightbox="./screenshots/8.png"' not in html and marker in html:
                html = html.replace(marker, additions)
            html = html.replace('VERSION LABEL: V6.0.0', 'VERSION LABEL: V6.1.0')
            index.write_text(html, encoding="utf-8", newline="\n")
    print(f"Copied V6.1 screenshots to {count} mapped repository paths and screenshots/v6.1/.")
    print("Updated the static website gallery to 9 entries if the prior gallery template was present.")
    print("Next: inspect `git status` and `git diff --stat`, then commit/push only after review.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
