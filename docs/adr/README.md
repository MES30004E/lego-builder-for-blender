# Architecture Decision Records

Architecture Decision Records, or ADRs, capture important project decisions and
the reasoning behind them.

No ADRs have been created yet.

## Why ADRs Exist

ADRs keep long-term decisions discoverable for maintainers, contributors, and
future AI agents.

Use ADRs when a decision affects architecture, supported platforms, public data
concepts, major dependencies, or long-term maintenance.

## ADR Numbering

Use sequential numbering:

```text
0001-short-title.md
0002-short-title.md
```

Do not reuse numbers.

## Decision Status

Use one of these statuses:

- Proposed
- Accepted
- Superseded
- Deprecated

## When to Create an ADR

Create an ADR when a decision is difficult to reverse, affects multiple modules,
or changes documented architecture.

Do not create ADRs for routine bug fixes, small documentation updates, or
temporary implementation details.

## ADR Template

```markdown
# ADR 0000: Title

## Status

Proposed

## Context

What problem or constraint led to this decision?

## Decision

What did the project decide?

## Consequences

What tradeoffs, follow-up work, or risks come from this decision?
```

## Rules for Creating ADRs

- Keep ADRs concise.
- Link related architecture or engineering docs.
- Do not rewrite accepted ADRs except to fix clarity.
- Supersede old ADRs with new ADRs when decisions change.

See [../ARCHITECTURE.md](../ARCHITECTURE.md) and
[../ENGINEERING.md](../ENGINEERING.md) for related project standards.
