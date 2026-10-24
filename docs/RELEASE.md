# Release artifact policy

A published application release should contain:

- The intended Windows executable, with filename and version identified in the release title/notes.
- A portable ZIP or documentation archive when the release format calls for it.
- A SHA-256 digest generated from the exact artifact attached to that release.
- A changelog and instructions that distinguish application changes from documentation/website changes.
- A screenshot set that reflects the same build as the executable.

The repository currently contains documentation, artwork, screenshots, a static website and release metadata. It does not contain the original application source tree. Do not describe a documentation commit as a source-code or binary modification.

## V6.1 publication checklist

1. Verify the intended binary and version.
2. Publish a `v6.1.0` tag/release. A separate release must have its own attached asset; files attached to `v6.0.0` do not automatically transfer.
3. Upload the intended executable and any release ZIP required for distribution.
4. Generate and publish SHA-256 for those exact uploaded files.
5. Confirm release title, tag, README, `VERSION`, download links and changelog agree before announcing the release.
