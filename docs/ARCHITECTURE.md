# Architecture

This document describes the high-level system design for LEGO Builder for
Blender. It defines architectural boundaries, not implementation details.

For product goals, see [PRODUCT.md](PRODUCT.md). For conceptual data flow, see
[DATA_MODEL.md](DATA_MODEL.md). For coding standards, see
[ENGINEERING.md](ENGINEERING.md).

## Overall Architecture

The project is a Blender Extension with a small Blender-facing entry point,
central registration, add-on preferences, user interface modules, pure library
validation helpers, and small utility modules.

The current implementation remains intentionally minimal: it supports extension
registration, a sidebar panel, add-on preferences, and basic LDraw path status.

## Module Boundaries

Future modules should keep responsibilities separate:

- `ui`: Blender panels, operators, menus, and user-facing presentation.
- `preferences`: user configuration and extension settings.
- `library`: pure library validation and future library-facing helpers.
- `utils`: small reusable helpers with no Blender UI ownership.
- `core`: LEGO building concepts independent of Blender UI.
- `ldraw`: LDraw library discovery, indexing, parsing, and metadata.
- `assets`: cached Blender representations of reusable parts.
- `materials`: LEGO color and material definitions.
- `snapping`: connection and placement rules.
- `io`: import, export, and interchange workflows.

Modules should be introduced only when real behavior needs them.

## Dependency Direction

Dependencies should point inward:

- Blender UI code may depend on domain and asset services.
- Preferences and panels may depend on pure validation helpers.
- Domain code should avoid direct UI dependencies.
- Data concepts should not depend on operators or panels.
- Import/export code should depend on documented data concepts, not UI state.

This keeps non-UI behavior testable and easier to reason about.

## Package Structure

The repository currently uses a root-level Blender Extension package with a
minimal `__init__.py` and focused support modules. As features arrive, package
structure should grow around stable responsibilities rather than speculative
layers.

The add-on entry point should remain responsible for:

- Extension metadata.
- Top-level registration and unregistration.
- Delegating feature wiring to the central registration module.

The central registration module should own Blender class registration order and
safe unregister behavior.

## Extension Boundaries

Blender API calls should be isolated near integration surfaces such as panels,
preferences, operators, and asset creation code.

Internal modules should prefer plain Python data structures where practical so
future tests can run without requiring Blender.

## Data Ownership

Data ownership should be explicit:

- LDraw libraries are external source data.
- Cached assets are generated project/runtime data.
- Placed instances belong to the active Blender scene.
- Connector relationships describe placement compatibility.
- The LDraw path preference is user configuration, not library content.

See [DATA_MODEL.md](DATA_MODEL.md) for terminology and lifecycle boundaries.

## Design Principles

- Keep registration code small and predictable.
- Prefer explicit boundaries over broad shared utilities.
- Add abstractions only when they clarify real behavior.
- Keep Blender-specific code easy to audit.
- Preserve a path toward testing core behavior outside Blender.
