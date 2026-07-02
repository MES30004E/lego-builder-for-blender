"""Workspace marker configuration helpers."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

CONFIG_FILENAME = "lego_builder_library.toml"
LEGACY_CONFIG_FILENAME = "lego_builder_workspace.toml"
CONFIG_SCHEMA_VERSION = 1
CONFIG_APPLICATION = "LEGO Builder"
CONFIG_WORKSPACE_VERSION = "0.4"


@dataclass(frozen=True)
class WorkspaceConfig:
    """Minimal marker config stored inside a LEGO Builder workspace."""

    schema_version: int
    application: str
    workspace_version: str
    created_with: str
    created_at: str


def get_workspace_config_path(workspace_path: Path) -> Path:
    """Return the marker config path for a workspace."""
    return workspace_path / CONFIG_FILENAME


def get_legacy_workspace_config_path(workspace_path: Path) -> Path:
    """Return the legacy marker config path for a workspace."""
    return workspace_path / LEGACY_CONFIG_FILENAME


def find_workspace_config_path(workspace_path: Path) -> Path | None:
    """Return the preferred available marker config path."""
    config_path = get_workspace_config_path(workspace_path)
    if config_path.is_file():
        return config_path

    legacy_config_path = get_legacy_workspace_config_path(workspace_path)
    if legacy_config_path.is_file():
        return legacy_config_path

    return None


def read_workspace_config(workspace_path: Path) -> WorkspaceConfig | None:
    """Read workspace marker config if it exists and is valid enough."""
    config_path = find_workspace_config_path(workspace_path)
    if config_path is None:
        return None

    try:
        data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError):
        return None

    schema_version = data.get("schema_version")
    application = data.get("application")
    workspace_version = data.get("workspace_version")
    created_with = data.get("created_with")
    created_at = data.get("created_at")
    values = (application, workspace_version, created_with, created_at)
    if not isinstance(schema_version, int):
        return None
    if not all(isinstance(value, str) for value in values):
        return None

    return WorkspaceConfig(
        schema_version=schema_version,
        application=application,
        workspace_version=workspace_version,
        created_with=created_with,
        created_at=created_at,
    )


def write_workspace_config(
    workspace_path: Path,
    created_with: str = "0.4.0",
) -> WorkspaceConfig:
    """Write the workspace marker config without touching unrelated files."""
    existing_config = read_workspace_config(workspace_path)
    created_at = (
        existing_config.created_at
        if existing_config is not None
        else datetime.now(UTC).isoformat()
    )
    config = WorkspaceConfig(
        schema_version=CONFIG_SCHEMA_VERSION,
        application=CONFIG_APPLICATION,
        workspace_version=CONFIG_WORKSPACE_VERSION,
        created_with=created_with,
        created_at=created_at,
    )
    config_path = get_workspace_config_path(workspace_path)
    config_path.write_text(
        "\n".join(
            (
                f"schema_version = {config.schema_version}",
                f'application = "{config.application}"',
                f'workspace_version = "{config.workspace_version}"',
                f'created_with = "{config.created_with}"',
                f'created_at = "{config.created_at}"',
                "",
            )
        ),
        encoding="utf-8",
    )
    return config


def has_valid_legacy_workspace_config(workspace_path: Path) -> bool:
    """Return whether a valid legacy marker config exists."""
    legacy_config_path = get_legacy_workspace_config_path(workspace_path)
    if not legacy_config_path.is_file():
        return False

    config_path = get_workspace_config_path(workspace_path)
    if config_path.exists():
        return False

    return read_workspace_config(workspace_path) is not None
