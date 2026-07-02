# Architecture

This document describes the high-level system design for LEGO Builder for
Blender. It defines architectural boundaries, not implementation details.

For product goals, see [PRODUCT.md](PRODUCT.md). For conceptual data flow, see
[DATA_MODEL.md](DATA_MODEL.md). For coding standards, see
[ENGINEERING.md](ENGINEERING.md).

## Overall Architecture

The project is a Blender Extension with a small Blender-facing entry point,
central registration, add-on preferences, user interface modules, pure library
validation/index helpers, pure LEGO Library helpers, runtime state, operator
modules, and small utility modules.

The current implementation remains intentionally focused: it supports extension
registration, a sidebar panel, add-on preferences, basic LDraw path status, a
refresh operator, LEGO Library folder management, and an in-memory LDraw part
metadata index.

The architecture introduced across `v0.2.0` and `v0.3.0` intentionally separates
Blender UI, Blender operators, pure Python library logic, runtime state, and the
future rendering pipeline. This separation is meant to support the future visual
asset browser and geometry importer without a major refactor.

Future UI architecture should distinguish between the current sidebar UI and a
dedicated workspace-level LEGO Builder UI. The sidebar remains the quick-control
surface, while the future workspace-like layout should host the primary building
experience.

## Module Boundaries

Future modules should keep responsibilities separate:

- `ui`: Blender panels, operators, menus, and user-facing presentation.
- `preferences`: user configuration and extension settings.
- `operators`: Blender operators that call pure project services.
- `library`: pure library validation, metadata extraction, and indexing.
- `workspace`: internal pure helpers for LEGO Library structure, validation,
  and marker config compatibility.
- `runtime`: in-memory session state such as the current workspace, current
  library, and current part index.
- `utils`: small reusable helpers with no Blender UI ownership.
- `core`: LEGO building concepts independent of Blender UI.
- `ldraw`: LDraw library discovery, indexing, parsing, and metadata.
- `assets`: cached Blender representations of reusable parts.
- `materials`: LEGO color and material definitions.
- `snapping`: connection and placement rules.
- `io`: import, export, and interchange workflows.
- Future rendering pipeline: mesh generation, materials, instancing, and scene
  organization once geometry import is designed.

Modules should be introduced only when real behavior needs them.

## Dependency Direction

Dependencies should point inward:

- Blender UI code may depend on domain and asset services.
- Preferences and panels may depend on pure validation helpers.
- Operators should call pure functions rather than own parsing logic.
- LEGO Library operators should call pure workspace services rather than owning
  filesystem rules.
- Runtime state should remain in memory only until persistence is explicitly
  designed.
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

Blender operators belong at the integration boundary. They should read Blender
context, call pure project functions, store results, and report concise status.

Future dedicated workspace UI code should remain a Blender integration layer. It
should coordinate panels, regions, operators, and runtime state without moving
library parsing, LEGO Library validation, indexing, snapping, or rendering logic
into UI code.

## Extension Boundaries

Blender API calls should be isolated near integration surfaces such as panels,
preferences, operators, and asset creation code.

Internal modules should prefer plain Python data structures where practical so
future tests can run without requiring Blender.

## Data Ownership

Data ownership should be explicit:

- LDraw libraries are external source data.
- The LEGO Library is user-selected durable project data.
- Part metadata is derived from `.dat` files and kept in memory.
- The part index is runtime state and is not persisted in v0.3.0.
- Cached assets are generated project/runtime data.
- Placed instances belong to the active Blender scene.
- Connector relationships describe placement compatibility.
- The LDraw path preference is user configuration, not library content.
- The LEGO Library folder preference points to durable project data, while the
  marker config identifies an initialized LEGO Library.
- Runtime state tracks current session selections and indexes, not durable user
  settings.

See [DATA_MODEL.md](DATA_MODEL.md) for terminology and lifecycle boundaries.

## Design Principles

- Keep registration code small and predictable.
- Prefer explicit boundaries over broad shared utilities.
- Add abstractions only when they clarify real behavior.
- Keep Blender-specific code easy to audit.
- Preserve a path toward testing core behavior outside Blender.
