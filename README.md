# LEGO Builder for Blender

LEGO Builder for Blender is an open-source Blender 5.1+ extension for building
LEGO models natively inside Blender.

## What It Is

The project aims to become a Blender-native LEGO building environment inspired
by dedicated LEGO design tools while taking advantage of Blender's modeling,
animation, and rendering capabilities.

## Current Status

Version 0.3.1 is a verified LDraw library index foundation with preferences UX
and CI compatibility fixes.

The extension currently provides a Blender sidebar panel, add-on preferences,
basic LDraw library path validation, and an in-memory `.dat` part metadata
index. LEGO building features such as geometry import, searchable asset
browsing, snapping, materials, caching, and export are not implemented yet.

## Installation

During early development, install the extension zip in Blender 5.1+ using
`Edit > Preferences > Extensions > Install from Disk`.

## Documentation

- [Project Context](docs/PROJECT_CONTEXT.md): current state and AI onboarding.
- [Vision](docs/VISION.md): why the project exists.
- [Product](docs/PRODUCT.md): what the product should become.
- [Roadmap](docs/ROADMAP.md): capability-based project direction.
- [Architecture](docs/ARCHITECTURE.md): high-level system design.
- [Data Model](docs/DATA_MODEL.md): conceptual data flow and ownership.
- [Engineering](docs/ENGINEERING.md): coding and quality standards.
- [Development Workflow](docs/DEVELOPMENT_WORKFLOW.md): feature and release flow.
- [Glossary](docs/GLOSSARY.md): canonical project terminology.
- [Architecture Decisions](docs/adr/README.md): ADR process.
- [Changelog](CHANGELOG.md): release history.

## Development Checks

Pull requests should pass the basic CI workflow in
[.github/workflows/ci.yml](.github/workflows/ci.yml). The workflow checks Python
syntax, Ruff, Black formatting, and project TOML parsing without requiring
Blender to be installed.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes.

## License

LEGO Builder for Blender is licensed under the [MIT License](LICENSE).
