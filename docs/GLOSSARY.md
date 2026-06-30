# Glossary

This document defines canonical terminology for LEGO Builder for Blender.

## Purpose

Use this glossary to keep product, architecture, code, and AI sessions aligned
on project language.

## Naming Conventions

- Use terms consistently across documentation and code.
- Prefer precise project terms over casual synonyms.
- Add new terms when they become part of project design.

## Canonical Definitions

### Brick

A physical LEGO element as understood by builders.

### Part

An LDraw definition or catalog-level shape that can be represented in Blender.

### Element

A specific LEGO catalog item, often combining part shape and color.

### Instance

One placed copy of a Part in a Blender scene.

### Asset

A reusable Blender representation of a Part or related resource.

### Cached Part

A generated reusable representation of a Part stored to avoid repeated work.

### Stud

A round raised connection feature on many LEGO bricks.

### Tube

An underside connection feature that can interact with studs.

### Connector

A conceptual connection point or relationship used by snapping and build logic.

### Library

An external collection of part definitions, such as an LDraw-compatible library.

### Build Session

The user's active modeling context while creating or editing LEGO structures.

### Illegal Connection

A connection that LEGO building rules or project-defined constraints consider
invalid. The project does not validate these yet.

## Things Intentionally Distinguished

- Brick is a builder-facing physical concept.
- Part is a reusable source definition.
- Element may imply a part plus color or catalog identity.
- Instance is a placed scene occurrence.
- Asset is a Blender-side reusable representation.

See [DATA_MODEL.md](DATA_MODEL.md) for conceptual data flow.
