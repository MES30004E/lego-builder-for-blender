# Engineering

This document defines coding and quality standards for LEGO Builder for
Blender.

## Python Standards

- Target Python 3.11+.
- Follow PEP 8.
- Prefer readable code over clever abstractions.
- Keep modules focused and small.

## Blender API Conventions

- Target Blender 5.1+.
- Keep registration and unregistration explicit.
- Isolate Blender API calls near integration boundaries.
- Avoid storing hidden state in Blender data without documentation.

## Type Hints

- Use type hints for public functions and non-obvious internal functions.
- Prefer standard Python types where practical.
- Do not add complex typing that obscures simple behavior.

## Documentation Style

- Document public modules, classes, and important workflows.
- Keep documents concise and cross-linked.
- Use [GLOSSARY.md](GLOSSARY.md) for canonical terminology.
- Update docs when behavior or architecture changes.

## Error Handling

- Prefer clear, actionable errors.
- Do not silently ignore missing libraries or invalid configuration.
- Keep user-facing messages concise.

## Logging

- Use logging for diagnostic information once runtime systems exist.
- Avoid noisy output during normal Blender use.
- Do not log sensitive local paths unless needed for troubleshooting.

## Performance Philosophy

- Design for large models, but optimize after behavior is clear.
- Prefer caching repeated part work.
- Measure before making performance-driven complexity permanent.

## Git Conventions

- Keep changes small and reviewable.
- Use clear commit messages.
- Do not rewrite published history without discussion.
- Keep generated artifacts out of source commits unless explicitly required.

## Testing Philosophy

- Test pure Python behavior outside Blender where possible.
- Manually verify Blender integration changes in supported Blender versions.
- Add automated tests as core behavior appears.

## Review Expectations

- Review for correctness, maintainability, and Blender API safety.
- Confirm documentation and changelog updates when behavior changes.
- Use ADRs for significant architectural decisions.

See [ARCHITECTURE.md](ARCHITECTURE.md) for system boundaries and
[DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md) for lifecycle expectations.
