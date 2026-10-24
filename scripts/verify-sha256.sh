#!/usr/bin/env bash
set -euo pipefail
if ! command -v sha256sum >/dev/null 2>&1; then
  echo "sha256sum is required." >&2; exit 2
fi
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file> <expected-sha256>" >&2; exit 2
fi
file="$1"
expected="${2,,}"
[ -f "$file" ] || { echo "File not found: $file" >&2; exit 1; }
actual="$(sha256sum "$file" | awk '{print $1}')"
printf 'Expected: %s\nActual:   %s\n' "$expected" "$actual"
[ "$actual" = "$expected" ] || { echo "FAIL: SHA-256 mismatch" >&2; exit 1; }
echo "PASS: SHA-256 matches"
