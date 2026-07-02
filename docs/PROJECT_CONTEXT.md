# Project Context

This is the onboarding document for future AI sessions and contributors. It
describes the current state of LEGO Builder for Blender.

## Current Project Status

Version 0.3.0 is complete. The extension installs and loads in Blender 5.1.2
with modular registration, add-on preferences, LDraw path validation, and an
in-memory LDraw part metadata index.

Geometry import, caching, search, thumbnails, materials, snapping, and export
are still not implemented.

## Current Milestone

`v0.4.0: Library Management`

## Completed Milestones

- `v0.1.0`: initial Blender Extension skeleton.
- `v0.2.0`: architecture refactor, add-on preferences, LDraw library path
  setting, and basic path validation.
- `v0.3.0`: pure LDraw metadata extraction, in-memory part indexing, refresh
  operator, and sidebar index status.
- Extension manifest.
- Minimal `LEGO` sidebar tab and `LEGO Builder` panel.
- Project README, license, build configuration, and changelog.

## Current Architecture Summary

The extension now uses a small modular structure with a minimal entry point,
central registration, add-on preferences, UI panels, pure LDraw path validation,
pure LDraw metadata/index helpers, LEGO Library validation/creation helpers,
runtime state, Blender operators, and utility helpers.

## Current Priorities

- Keep the project installable in Blender 5.1+.
- Keep the LEGO sidebar tab working.
- Preserve modular registration and safe unregister behavior.
- Provide an optional LDraw library path preference.
- Keep basic LDraw path validation pure Python and free of `bpy`.
- Plan a managed LDraw library experience.
- Provide a durable LEGO Library foundation.
- Keep LEGO Library structure, validation, and marker config logic pure Python.
- Preserve pure Python validation, metadata extraction, and index building.
- Store the part index in memory only until persistent indexing is designed.
- Keep runtime state in memory only.
- Preserve the long-term direction toward a dedicated LEGO Builder
  workspace-like Blender UI without implementing it yet.
- Avoid claiming support for unimplemented LEGO workflows.

## Current Constraints

- Blender 5.1+ is the target runtime.
- Python 3.11+ is the target Python version.
- The project should remain suitable for Blender Extensions distribution.
- Changes should be small, reviewable, and documented.
- Blender add-on preferences may be reset when uninstalling or reinstalling the
  extension.
- Future durable project data should live in a user-selected LEGO Library rather
  than only in Blender add-on preferences.
- A future LEGO Library manager should own LDraw library download/setup and cache
  folder management.
- v0.4 introduces LEGO Library folder creation and a marker config, but does not
  download LDraw libraries or manage updates yet.
- The LEGO Library marker config identifies the library and must not store
  user-specific settings.

## Supported Runtime

- Blender: 5.1+
- Python: 3.11+

## Important Engineering Decisions

- Start as a Blender Extension, not just an importer.
- Keep `__init__.py` minimal and registration-focused.
- Prefer modular boundaries over premature implementation.
- Record significant architecture choices using the ADR process in
  [adr/README.md](adr/README.md).

## Known Technical Debt

- No automated test suite exists yet.
- Blender CLI validation is not available in the current development shell.
- GitHub publishing requires local authentication outside this environment.

## AI Workflow

Every implementation session should begin by reading:

1. `PROJECT_CONTEXT.md`
2. `ENGINEERING.md`
3. `ARCHITECTURE.md`
4. Relevant ADRs in `adr/`
5. `ROADMAP.md`

Then inspect the current worktree before making changes.

## Never Assume

- Do not assume LDraw importing exists.
- Do not assume basic path validation means full LDraw validation.
- Do not assume the in-memory part index represents geometry.
- Do not assume v0.4 library management includes downloads, updates, additional
  directories, or multiple library locations beyond the LEGO Library foundation.
- Do not assume v0.5 visual asset browsing, thumbnails, search, or drag-and-drop
  exist.
- Do not assume v0.6 geometry import, mesh generation, material generation, or
  primitive substitution exists.
- Do not assume a dedicated LEGO Builder Blender workspace or layout exists.
- Do not assume runtime state persists after Blender reloads the extension.
- Do not assume parts, materials, snapping, caching, export, or build tools work.
- Do not assume a planned module exists until it appears in the repository.
- Do not assume Blender is available in the shell.

## Never Change Without Discussion

- Supported Blender or Python versions.
- Extension identity or manifest compatibility.
- Licensing.
- Public roadmap direction.
- Architecture boundaries documented in [ARCHITECTURE.md](ARCHITECTURE.md).
