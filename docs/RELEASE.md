# Release artifact policy

Each release should include:
- A versioned Windows executable
- A portable ZIP containing the executable and documentation
- A SHA-256 manifest for integrity checking
- Release notes that distinguish packaging changes from application feature changes

Do not describe an EXE-only package as the original source code. If source files become available, add the real source tree, dependency/build instructions, and a reproducible build workflow.
