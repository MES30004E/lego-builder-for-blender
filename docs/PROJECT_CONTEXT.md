# Project Context

This is the onboarding document for future AI sessions and contributors. It
describes the current state of LEGO Builder for Blender.

## Current Project Status

Version 0.1.0 is complete. The extension installs and loads in Blender 5.1.2
with a minimal sidebar panel.

No LEGO building features are implemented yet.

## Current Milestone

The project is preparing the documentation and architecture foundation for
future feature work.

## Completed Milestones

- `v0.1.0`: initial Blender Extension skeleton.
- Extension manifest.
- Minimal `LEGO` sidebar tab and `LEGO Builder` panel.
- Project README, license, build configuration, and changelog.

## Current Architecture Summary

The current extension has a single Blender entry point. Future modules are
described in [ARCHITECTURE.md](ARCHITECTURE.md) but should not be created until
real behavior needs them.

## Current Priorities

- Keep the project installable in Blender 5.1+.
- Preserve a clean documentation foundation.
- Introduce feature modules gradually.
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

- Do not assume LDraw integration exists.
- Do not assume parts, materials, snapping, caching, export, or build tools work.
- Do not assume a planned module exists until it appears in the repository.
- Do not assume Blender is available in the shell.

## Never Change Without Discussion

- Supported Blender or Python versions.
- Extension identity or manifest compatibility.
- Licensing.
- Public roadmap direction.
- Architecture boundaries documented in [ARCHITECTURE.md](ARCHITECTURE.md).
