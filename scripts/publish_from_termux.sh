#!/usr/bin/env bash
set -Eeuo pipefail

# Publish reviewed repository changes from Termux. This script does not build or
# publish an executable and does not create a GitHub Release/tag.
REPO_URL="${ROM_FLASHER_REPO_URL:-https://github.com/xboyrex/ROM-Flasher-Pro-by-Mayank-Droid.git}"
BRANCH="${ROM_FLASHER_BRANCH:-main}"
COMMIT_MESSAGE="${1:-docs: refresh V6.1 screenshots and release metadata}"

command -v git >/dev/null 2>&1 || { echo "ERROR: git is missing. Install with: pkg install git"; exit 1; }
command -v python >/dev/null 2>&1 || { echo "ERROR: python is missing. Install with: pkg install python"; exit 1; }

SOURCE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT="${ROM_FLASHER_REPO_DIR:-$HOME/ROM-Flasher-Pro-by-Mayank-Droid}"

if [ -d "$SOURCE_ROOT/.git" ]; then
  # Script is running inside the target Git checkout.
  ROOT="$SOURCE_ROOT"
else
  # Script is running from the downloaded update ZIP (which intentionally has no .git).
  if [ ! -d "$ROOT/.git" ]; then
    echo "Target checkout not found at: $ROOT"
    echo "Clone the GitHub repository now? [y/N]"
    read -r answer
    case "$answer" in y|Y|yes|YES) git clone "$REPO_URL" "$ROOT" ;; *) echo "Cancelled."; exit 1 ;; esac
  fi
  echo "Copy refreshed package files from:"
  echo "  $SOURCE_ROOT"
  echo "into Git checkout:"
  echo "  $ROOT"
  echo "This overwrites files with matching names but leaves the checkout's .git directory intact."
  echo "Continue with overlay? [y/N]"
  read -r answer
  case "$answer" in y|Y|yes|YES) ;; *) echo "Cancelled before copying."; exit 0 ;; esac
  # The source bundle intentionally contains no .git directory.
  cp -a "$SOURCE_ROOT"/. "$ROOT"/
fi

cd "$ROOT"
git remote get-url origin >/dev/null 2>&1 || { echo "ERROR: origin remote is not configured."; exit 1; }

echo "== Repository =="
git remote -v
echo "== Current branch/status =="
git status --short --branch
echo
echo "== Validate documentation/site assets =="
python -m unittest discover -s tests -v
python - <<'PY'
from pathlib import Path
import re
import xml.etree.ElementTree as ET
root = Path(".")
site = root / "website"
html = (site / "index.html").read_text(encoding="utf-8")
missing = []
for value in re.findall(r'(?:src|href|data-lightbox)="(\./(?:assets|screenshots)/[^"]+)"', html):
    target = site / value.removeprefix("./")
    if not target.is_file():
        missing.append(str(target))
if missing:
    raise SystemExit("Missing website assets:\n" + "\n".join(missing))
for svg in list((root / "assets").rglob("*.svg")) + list((site / "assets").rglob("*.svg")):
    ET.parse(svg)
print("Website local references and SVG XML: OK")
PY

echo
echo "Review changes before publishing. This script stages all tracked/untracked changes in this repository."
git diff --check
git diff --stat
echo
echo "Continue to stage, commit and push to origin/$BRANCH? [y/N]"
read -r answer
case "$answer" in y|Y|yes|YES) ;; *) echo "Cancelled before staging/commit/push."; exit 0 ;; esac

git add -A
if git diff --cached --quiet; then
  echo "No staged changes to commit."
  exit 0
fi
git diff --cached --check
git commit -m "$COMMIT_MESSAGE"
git push origin "HEAD:$BRANCH"
echo
echo "Push completed. Verify the GitHub Actions/deployment result in the repository."
echo "NOTE: No executable or GitHub Release was created by this script."
