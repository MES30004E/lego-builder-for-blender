# Architecture

LEGO Builder for Blender is intended to grow into a Blender-native LEGO
building environment. The project should stay modular enough to support that
goal without making the first milestones heavier than they need to be.

## Current Shape

Version 0.1 contains only the add-on entry point:

- `__init__.py` defines Blender add-on metadata.
- `__init__.py` registers and unregisters the initial sidebar panel.
- No LEGO building functionality exists yet.

This keeps the first milestone easy to install, inspect, and replace as the
project structure becomes more complete.

## Design Principles

- Keep Blender registration code small and predictable.
- Prefer focused modules over a large add-on entry file.
- Use type hints and docstrings for public functions and classes.
- Add abstractions only when they clarify real behavior.
- Keep feature milestones small enough to review and test independently.

## Planned Module Boundaries

Future work should split responsibilities into dedicated packages:

- `ui`: panels, menus, operators, and Blender-facing presentation code.
- `core`: domain models and building rules independent of Blender UI.
- `assets`: brick libraries, materials, and reusable data loading helpers.
- `io`: import, export, and interchange formats.
- `preferences`: add-on settings and user configuration.

These modules should be introduced only when the first behavior in each area is
implemented.

## Blender Integration

The add-on entry point should remain responsible for:

- `bl_info` metadata.
- Registering and unregistering classes.
- Wiring top-level modules into Blender.

Feature modules should expose explicit registration helpers once they exist, so
Blender API calls stay easy to audit.
