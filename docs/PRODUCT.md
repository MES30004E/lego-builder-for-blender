# Product

This document defines the intended product experience. It does not describe how
features are implemented.

## Target Users

- LEGO builders who want Blender rendering and presentation workflows.
- Blender users who want LEGO-aware modeling tools.
- Open-source contributors interested in LEGO, 3D assets, and Blender tools.
- Advanced users who need exportable, optimized LEGO scenes.

## Primary Workflows

- Configure a LEGO part library.
- Search for parts.
- Place and adjust parts in a Blender scene.
- Use snapping and connection guidance.
- Apply LEGO-aware materials.
- Optimize large LEGO scenes.
- Render or export completed models.

## Long-Term UX Direction

LEGO Builder should eventually feel like a dedicated Blender-native LEGO
building environment, not only a sidebar add-on.

The sidebar should remain useful for quick controls, status, and lightweight
actions. The main building experience should eventually happen in a dedicated
workspace-like layout inside Blender.

That workspace-like experience should support part browsing, snapping, collision
feedback, build tools, color and material controls, and object inspection.

The current v0.4 LEGO Library foundation is storage and setup infrastructure
only; it does not create the dedicated Blender workspace or building layout.

## Core Capabilities

- LDraw library integration.
- Searchable part browser.
- Cached part assets.
- LEGO material mapping.
- Snapping and connection support.
- Build tools for repeated placement workflows.
- Scene optimization for large models.
- Export and presentation workflows.

These are product goals, not current feature claims.

## User Experience Principles

- Building should feel predictable.
- Blender conventions should be respected.
- LEGO-specific tools should stay discoverable.
- The dedicated building workspace should feel focused without hiding normal
  Blender power-user workflows.
- Heavy scenes should remain manageable.
- Errors should explain what users can do next.

## Feature Categories

- Library setup and indexing.
- LEGO Library management.
- Part discovery.
- Placement and snapping.
- Materials and visual fidelity.
- Scene management and optimization.
- Import, export, and interoperability.

## Out-of-Scope Features

- Proprietary LEGO service integration without explicit design approval.
- A custom modeling engine outside Blender.
- Gameplay or simulation features unrelated to building.
- Claims of legal build validation until connection rules are designed.

See [VISION.md](VISION.md) for philosophy and [ROADMAP.md](ROADMAP.md) for
capability sequencing.
