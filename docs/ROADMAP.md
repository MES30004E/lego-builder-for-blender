# Roadmap

This is a capability-based roadmap. It is not a detailed implementation plan.

## Current Roadmap Status

`v0.1.0` established the extension skeleton. `v0.2.0` added architecture and
preferences. `v0.3.0` added the pure LDraw library index foundation.

## Foundation

Expected milestone: `v0.2`

- Establish package structure.
- Add preferences foundation.
- Add basic LDraw library path validation.
- Add basic verification workflow.
- Keep documentation current.

## LDraw Integration

Expected milestone: `v0.2` to `v0.3`

- Configure an LDraw library path.
- Discover library availability.
- Read enough metadata to support later browsing.
- Build an in-memory index of `.dat` part metadata.

## Library Management

Expected milestone: `v0.4`

- Let users select where LEGO Builder stores library data.
- Automatically create the required folder structure.
- Download the official LDraw library from official sources.
- Verify downloaded library integrity.
- Detect missing or corrupted libraries.
- Update an existing library.
- Support multiple library locations.
- Provide a library manager UI.
- Show library size and statistics.

This is not implemented in `v0.3.0`. Manual creation of `parts/` and `p/`
folders should eventually no longer be required.

## Part Browser

Expected milestone: `v0.5`

- Provide a modern visual LEGO asset browser inspired by asset browser patterns
  such as Polligon and Blender's built-in Asset Browser, with original
  implementation and UI.
- Show a thumbnail grid and brick preview images.
- Provide search, category filters, color filters, sorting, favorites, recently
  used parts, and a part information panel.
- Support pagination or virtual scrolling.
- Support configurable thumbnail sizes.
- Prepare for drag-and-drop import and double-click import.
- Prepare for background thumbnail generation, background indexing, incremental
  refresh, and optional thumbnail caching.

This is not implemented in `v0.3.0`; no asset browser UI, thumbnails, rendering,
search, or import controls exist yet.

## Geometry Import

Expected milestone: `v0.6`

- Parse LDraw geometry.
- Generate Blender meshes.
- Generate materials.
- Map LEGO colors.
- Support stud logos.
- Support primitive substitution.
- Support instancing and collection management.
- Provide import options.
- Prioritize performance optimization.

This is not implemented in `v0.3.0`; the current part index is metadata only.

## Search and Filtering

Expected milestone: `v0.5`

- Search and filter indexed parts.
- Show part metadata.
- Prepare for placement workflows.

## Materials

Expected milestone: `v0.4`

- Map LEGO colors to Blender materials.
- Keep material handling reusable.
- Support consistent visual output.

## Snapping Engine

Expected milestone: future.

- Represent connectors.
- Guide compatible placement.
- Avoid claiming legal build validation before rules are designed.

## Build Tools

Expected milestone: future.

- Place and transform parts efficiently.
- Support repeated building workflows.
- Keep tools aligned with Blender interaction patterns.

## Scene Optimisation

Expected milestone: future.

- Reduce overhead for large LEGO scenes.
- Reuse cached assets where appropriate.
- Preserve visual quality and editability.

## Rendering

Expected milestone: future.

- Support high-quality presentation workflows.
- Respect Blender rendering pipelines.
- Keep materials and scene organization renderer-friendly.

## Export

Expected milestone: future.

- Export useful model representations.
- Preserve part and instance information where possible.
- Document limitations clearly.

## Future Ideas

- Build instruction support.
- Model analysis tools.
- Collaboration workflows.
- Advanced library metadata.

See [PRODUCT.md](PRODUCT.md) for product scope and
[DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) for how roadmap items become
work.
