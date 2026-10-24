# Publish from Termux

This helper publishes the reviewed repository changes to the configured GitHub repository. It does **not** build an EXE, create a release tag, or upload a release asset.

## 1. Install prerequisites

```bash
pkg update
pkg install git python
```

## 2. Put the refreshed project in Termux

Extract the project ZIP into a directory. If it is under Android Downloads, grant Termux storage access first:

```bash
termux-setup-storage
```

Run the publishing script from the extracted project folder. If that folder is not a Git checkout, the script clones the target repository into `~/ROM-Flasher-Pro-by-Mayank-Droid`, then asks permission to overlay the refreshed files into that clone. It never overwrites the `.git` directory.

## 3. Authenticate GitHub

Use an SSH key or GitHub CLI credential setup already configured for your account. Do not put a personal access token directly in the script, command history, or repository files. For HTTPS, GitHub password authentication is not supported; use a secure credential helper or switch the `origin` remote to SSH.

## 4. Review, test and push

From the extracted update ZIP folder (or the target Git checkout):

```bash
chmod +x scripts/publish_from_termux.sh
bash scripts/publish_from_termux.sh "docs: refresh V6.1 screenshots and release metadata"
```

The script validates Python tests, local website assets and SVG XML, then displays the diff summary. When launched from the update ZIP, it asks before overlaying files into the Git checkout. It asks again before staging, committing and pushing to `origin/main`. It stages all repository changes, so inspect `git status` and do not proceed if unrelated files are present.

To use a different checkout path or branch:

```bash
export ROM_FLASHER_REPO_DIR="$HOME/path/to/ROM-Flasher-Pro-by-Mayank-Droid"
export ROM_FLASHER_BRANCH="main"
bash scripts/publish_from_termux.sh
```

## 5. Release checklist

- Confirm the pushed commit and website deployment on GitHub.
- Build the application from its actual source tree and test it on supported device/firmware combinations.
- Calculate SHA-256 for the exact final EXE/package.
- Only then create a `v6.1.0` GitHub Release and attach that verified artifact. Do not rename a previous-version executable to imply it is a new build.
