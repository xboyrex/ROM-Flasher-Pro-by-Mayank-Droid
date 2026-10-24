#!/usr/bin/env python3
"""Apply the seven unique screenshots from the supplied Screenshots.zip.

Usage:
  python scripts/apply_v61_screenshots.py /path/to/Screenshots.zip --repo .
The byte-identical Screenshot (72).png is deliberately excluded. Existing RAM
Cleaner art is retained because the supplied archive has no replacement for it.
"""
from __future__ import annotations
import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

MAP = {
    "Screenshot (66).png": (1, "aosp-custom-rom.png"),
    "Screenshot (67).png": (2, "hyperos-miui-miflash.png"),
    "Screenshot (68).png": (3, "kernel-recovery.png"),
    "Screenshot (69).png": (4, "terminal-console-idle.png"),
    "Screenshot (70).png": (5, "driver-installation.png"),
    "Screenshot (71).png": (6, "tool-verification-console.png"),
    "Screenshot (73).png": (7, "official-links.png"),
}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path, help="Uploaded Screenshots.zip")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()
    repo, archive = args.repo.resolve(), args.archive.resolve()
    if not archive.is_file():
        raise SystemExit(f"Screenshot archive not found: {archive}")
    with tempfile.TemporaryDirectory(prefix="romflasher-v61-") as tmp:
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(tmp)
        matches = list(Path(tmp).rglob("Screenshot (66).png"))
        if not matches:
            raise SystemExit("Could not find Screenshot (66).png in the archive.")
        src_dir = matches[0].parent
        missing = [name for name in MAP if not (src_dir / name).is_file()]
        if missing:
            raise SystemExit("Archive missing required files: " + ", ".join(missing))
        seen = {}
        for filename, (number, semantic) in MAP.items():
            src = src_dir / filename
            digest = hashlib.sha256(src.read_bytes()).hexdigest()
            seen[filename] = digest
            destinations = [
                repo / f"{number}.png",
                repo / "main" / f"{number}.png",
                repo / "website" / "screenshots" / f"{number}.png",
                repo / "docs" / "readme-screenshots" / semantic,
                repo / "docs" / "readme-screenshots" / f"{number}.png",
                repo / "screenshots" / "v6.1" / semantic,
            ]
            for dest in destinations:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
        duplicate = hashlib.sha256((src_dir / "Screenshot (72).png").read_bytes()).hexdigest()
        if duplicate != seen["Screenshot (70).png"]:
            print("WARNING: Screenshot (72).png is no longer identical to Screenshot (70).png; review it manually.")
        else:
            print("Confirmed duplicate excluded: Screenshot (72).png == Screenshot (70).png")
        manifest = repo / "screenshots" / "v6.1" / "SHA256SUMS.txt"
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text("".join(f"{digest}  {MAP[name][1]}\n" for name, digest in seen.items()), encoding="utf-8")
    print(f"Applied {len(MAP)} unique screenshots. Review git diff before committing.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
