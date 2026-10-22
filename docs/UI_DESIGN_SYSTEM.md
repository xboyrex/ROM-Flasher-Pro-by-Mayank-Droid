# UI design system

## Visual direction

- **Theme:** dark graphite workbench, cyan technical accents, violet secondary accents and amber destructive-action warnings.
- **Typography:** platform system stack for predictable rendering; monospace reserved for telemetry, labels and status.
- **Structure:** clear hierarchy, strong action grouping, compact status metadata and responsive layouts.
- **Icons:** bundled, local, 24×24 stroke-based SVG icons; no remote icon font or runtime icon CDN is required.
- **Motion:** short, restrained hover transitions with `prefers-reduced-motion` support.

## Tokens

| Token | Value | Use |
|---|---|---|
| Background | `#080b12` | Site canvas |
| Panel | `#101725` | Cards and UI surfaces |
| Border | `#263248` | Separators and cards |
| Text | `#f3f6fd` | High-priority text |
| Muted | `#9eabc2` | Explanatory copy |
| Cyan | `#50e5f2` | Primary technical accent |
| Violet | `#a58aff` | Secondary accent |
| Green | `#78f0bd` | Ready/status decoration only |
| Amber | `#ffc974` | Risk/destructive-action notices |

## Interaction and accessibility

- All actions are real links or buttons with visible focus indicators.
- Mobile navigation exposes its expanded state.
- Workspace tabs support click and keyboard arrow navigation.
- Gallery filters expose their pressed state and update the visible count.
- Screenshot previews use a native dialog lightbox with Escape-to-close behavior.
- Decorative images use empty alternative text; screenshots include descriptive alt text.
- Reduced-motion preferences are respected.

## Scope note

This design system governs the static project website and repository documentation. It does not modify the compiled Windows executable UI or establish that controls in the executable function correctly.
