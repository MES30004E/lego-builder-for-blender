# Data Model

This document explains conceptual project data. It does not define schemas,
storage formats, or algorithms.

## Conceptual Flow

```text
LDraw Part
    ↓
Cached Blend Asset
    ↓
Placed Instance
    ↓
Connector Graph
    ↓
Scene
```

## LDraw Part

An LDraw Part is a source definition from an external LDraw-compatible library.
It is library data, not Blender scene data.

## Cached Blend Asset

A Cached Blend Asset is a reusable Blender representation generated from part
source data. It exists to avoid rebuilding the same part repeatedly.

## Placed Instance

A Placed Instance is one occurrence of a part in a Blender scene. It owns
placement, scene organization, and user-facing edit state.

## Connector Graph

A Connector Graph describes possible relationships between placed instances,
such as studs, tubes, and other connection points.

It is a conceptual model for build behavior and should not be treated as legal
connection validation until that behavior is explicitly designed.

## Scene

The Scene is the Blender-owned result of placed instances, materials, objects,
collections, and user edits.

## Ownership and Lifecycle

- LDraw Parts come from an external library.
- Cached Blend Assets are generated and may be refreshed.
- Placed Instances belong to a Blender scene.
- Connector Graph data belongs to building logic.
- Scene data remains under Blender ownership.

## Related Documents

- [GLOSSARY.md](GLOSSARY.md) defines canonical terms.
- [ARCHITECTURE.md](ARCHITECTURE.md) defines module boundaries.
- [ROADMAP.md](ROADMAP.md) describes capability sequencing.
