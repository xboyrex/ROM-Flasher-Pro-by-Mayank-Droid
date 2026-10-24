# Changelog

## V6.1.0 — Hotfix documentation and screenshot refresh

The V6.1.0 hotfix record consolidates the supplied build notes without repeating the same issue under multiple headings. Reported areas include UI redraw stability, ADB/Fastboot state handling, package auto-routing, large-ROM sideload streaming, console readability, driver/tool verification and RAM Cleaner stages.

- **UI:** state-signature redraw guard, steadier tab repainting, static status text, on-demand progress animation and a simplified Fastboot action area.
- **Device state:** direct ADB-server TCP polling, explicit refresh-driven scan/reset behavior and improved Recovery/ADB-sideload/Fastboot state separation.
- **Package detection:** metadata-first payload partition discovery and automatic routing for supported ZIP/TGZ/IMG inputs, including AOSP payload ZIPs selected from the HyperOS workflow.
- **Large sideload:** reported 64 KiB chunked transfer path, ADB_TRACE cleanup and quieter payload extraction output.
- **Console:** read-only output, consistent newline handling, improved wrapping and removal of the repeated RAM-BOOST prefix.
- **Drivers/tools:** driver installation panel and console verification for the listed driver groups and bundled utilities.
- **RAM Cleaner:** ten reported stages, including heap/GC and temporary/USB-buffer cleanup.
- **Build notes:** reported syntax-warning fixes and startup initialization checks.

Detailed technical list: [`CHANGELOG.txt`](CHANGELOG.txt). Workflow-specific guidance: [`INSTRUCTIONS.txt`](INSTRUCTIONS.txt).

> Evidence boundary: the original application source tree is not present in this repository. Application changes above are taken from the supplied build notes and could not be independently verified from source during this repository update. The V6.1.0 GitHub Release must be published separately from this documentation commit.

## V6.0.0 — documentation and website refresh

- Reworked the repository README into a screenshot-led project guide.
- Updated the static website with responsive layout, local vector icons, workspace explorer, screenshot filtering and image lightbox.
- Added a feature guide, installation guidance, release-artifact policy and verification instructions.
- Added UI design notes, static integrity checks and website deployment documentation.
