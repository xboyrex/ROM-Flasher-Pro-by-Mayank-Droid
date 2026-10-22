# ROM Flasher Pro — static website

A responsive, dependency-free website and interface documentation gallery for ROM Flasher Pro by Mayank Droid.

## Preview locally

Open `index.html` in a modern browser. No Node install, package manager or build command is required. All CSS, JavaScript, SVG icons and screenshot images are bundled in this directory.

## Cloudflare Pages

Create or edit the Pages project settings:

- **Production branch:** `main`
- **Root directory:** `website`
- **Framework preset:** `None`
- **Build command:** leave empty
- **Build output directory:** `.`

The site uses relative paths, so `website/` can be deployed as a self-contained static directory. Feature and installation links point to the repository docs on GitHub, so they continue to work when `website/` is deployed as a standalone static root.

## Included features

- Responsive desktop/mobile header and accessible mobile navigation.
- Feature cards for AOSP, HyperOS/MIUI, Kernel & Recovery, Terminal Console, RAM Cleaner and device status.
- Interactive workspace explorer using the included screenshots.
- Filterable screenshot gallery with a native dialog lightbox.
- Local SVG icon set, no icon CDN dependency.
- Reduced-motion support, visible focus states and semantic sections.

## Important

This is a product site/documentation layer. It does not connect to a phone, execute ADB/Fastboot commands, flash firmware or modify Windows memory. The screenshots represent the provided app UI. Confirm the executable's real behavior independently.
