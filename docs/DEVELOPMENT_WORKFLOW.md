# Development Workflow

This document defines how project work moves from idea to release.

## Feature Lifecycle

```text
Idea
  ↓
Design
  ↓
Specification
  ↓
Implementation
  ↓
Verification
  ↓
Blender Testing
  ↓
Review
  ↓
Release
```

## Idea

Start with the user problem, project goal, and relevant roadmap capability.

## Design

Decide the shape of the change before writing code. Check
[ARCHITECTURE.md](ARCHITECTURE.md) and existing ADRs.

## Specification

Define expected behavior, in-scope work, out-of-scope work, and verification
steps.

## Implementation

Keep changes small, modular, and reviewable. Follow
[ENGINEERING.md](ENGINEERING.md).

## Verification

Run checks appropriate to the change, including syntax, configuration, tests,
and documentation link checks.

## Blender Testing

For Blender-facing changes, test install, enable, register, unregister, and the
affected UI or scene workflow in a supported Blender version.

## Review

Review correctness, maintainability, user impact, documentation, and whether an
ADR is needed.

## Release

Update [CHANGELOG.md](../CHANGELOG.md), verify packaging, create intentional
tags, and publish only after the release state is clear.

## Definition of Done

A change is done when it is implemented, verified, documented, and reviewable.

## Release Checklist

- Version and changelog are correct.
- Extension metadata is valid.
- Blender install/load behavior is verified.
- Documentation reflects the release state.
- Tags and release artifacts are intentional.

## Documentation Update Policy

Documentation should change with the project. Prefer updating the canonical doc
instead of repeating information elsewhere.

## Documentation Ownership Rule

A feature is not complete until:

- Code updated.
- Tests updated.
- Documentation updated.
- `CHANGELOG.md` updated.
- Architecture updated if required.
- ADR added if required.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contributor expectations.
