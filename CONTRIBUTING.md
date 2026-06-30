# Contributing

Thank you for helping build LEGO Builder for Blender. This project is young, so
small, well-documented changes are preferred.

Before changing code, read [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md)
and [docs/ENGINEERING.md](docs/ENGINEERING.md).

## Development Setup

- Use Blender 5.1 or newer for manual extension testing.
- Use Python 3.11 or newer for local tooling.
- Keep the extension installable from the repository or a packaged zip.
- Do not assume LEGO building features exist unless documented in
  [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md).

## Branch Strategy

- Use short-lived feature branches.
- Keep each branch focused on one reviewable change.
- Avoid mixing documentation, refactors, and feature work unless the change
  requires it.

## Commit Message Style

- Use clear, imperative commit messages.
- Mention the area changed when helpful.
- Keep version tags for intentional releases only.

Example:

```text
Add documentation foundation
```

## Pull Request Expectations

- Explain the goal of the change.
- List verification performed.
- Note any Blender version used for manual testing.
- Link relevant roadmap items or ADRs when applicable.
- Keep the diff small enough to review carefully.

## Local Verification

Before opening a pull request, run checks appropriate to the change:

- Python syntax checks for changed Python files.
- TOML parsing checks for manifest or project metadata changes.
- Blender install/load checks for extension behavior changes.
- Link and scope checks for documentation changes.

## Documentation Expectations

Documentation is part of the product. Update docs when behavior, architecture,
workflow, terminology, or project status changes.

Use [docs/GLOSSARY.md](docs/GLOSSARY.md) for canonical terms and
[docs/DEVELOPMENT_WORKFLOW.md](docs/DEVELOPMENT_WORKFLOW.md) for the full
feature lifecycle.
