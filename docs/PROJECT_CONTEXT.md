# Project Context

This is the onboarding document for future AI sessions and contributors. It
describes the current state of LEGO Builder for Blender.

## Current Project Status

Version 0.1.0 is complete. The extension installs and loads in Blender 5.1.2
with a minimal sidebar panel.

The v0.2.0 architecture and preferences foundation is in progress. LEGO
building features are still not implemented.

## Current Milestone

`v0.2.0: Architecture Refactor & Preferences`

## Completed Milestones

- `v0.1.0`: initial Blender Extension skeleton.
- Extension manifest.
- Minimal `LEGO` sidebar tab and `LEGO Builder` panel.
- Project README, license, build configuration, and changelog.

## Current Architecture Summary

The extension now uses a small modular structure with a minimal entry point,
central registration, add-on preferences, UI panels, pure LDraw path validation,
and utility helpers.

## Current Priorities

- Keep the project installable in Blender 5.1+.
- Keep the LEGO sidebar tab working.
- Preserve modular registration and safe unregister behavior.
- Provide an optional LDraw library path preference.
- Keep basic LDraw path validation pure Python and free of `bpy`.
- Avoid claiming support for unimplemented LEGO workflows.

## Current Constraints

- Blender 5.1+ is the target runtime.
- Python 3.11+ is the target Python version.
- The project should remain suitable for Blender Extensions distribution.
- Changes should be small, reviewable, and documented.

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
- Do not assume parts, materials, snapping, caching, export, or build tools work.
- Do not assume a planned module exists until it appears in the repository.
- Do not assume Blender is available in the shell.

## Never Change Without Discussion

- Supported Blender or Python versions.
- Extension identity or manifest compatibility.
- Licensing.
- Public roadmap direction.
- Architecture boundaries documented in [ARCHITECTURE.md](ARCHITECTURE.md).
