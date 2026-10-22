# Release artifact policy

Each release should include:
- A versioned Windows executable.
- A portable ZIP containing the executable and user documentation, when applicable.
- A SHA-256 manifest for the exact release artifacts.
- Release notes that separate packaging/documentation updates from actual application feature changes.

The public repository currently contains docs, artwork, screenshots, a static website and checksum metadata. It does not contain the original application source tree or the Windows executable. Do not describe documentation/UI website work as a binary feature change. If the original source becomes available, add the real source tree, dependency/build instructions and reproducible-build workflow.
