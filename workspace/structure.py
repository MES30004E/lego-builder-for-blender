"""Workspace folder structure helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

try:
    from ..utils.paths import normalize_optional_path
except ImportError:  # Allows local tests to import this module outside Blender.
    from utils.paths import normalize_optional_path

try:
    from .config import (
        get_workspace_config_path,
        has_valid_legacy_workspace_config,
        read_workspace_config,
        write_workspace_config,
    )
except ImportError:  # Allows local tests to import this module outside Blender.
    from workspace.config import (
        get_workspace_config_path,
        has_valid_legacy_workspace_config,
        read_workspace_config,
        write_workspace_config,
    )

WORKSPACE_DIRECTORIES = (
    Path("ldraw") / "parts",
    Path("ldraw") / "p",
    Path("ldraw") / "unofficial",
    Path("ldraw") / "models",
    Path("cache") / "metadata",
    Path("cache") / "geometry",
    Path("cache") / "thumbnails",
    Path("downloads"),
    Path("projects"),
    Path("logs"),
)


@dataclass(frozen=True)
class WorkspaceCreationResult:
    """Result of creating a LEGO Builder workspace structure."""

    is_success: bool
    message: str
    path: Path | None
    created_paths: tuple[Path, ...]


def get_workspace_ldraw_path(workspace_path: str | Path | None) -> Path | None:
    """Return the LDraw folder inside a workspace path."""
    normalized_path = normalize_optional_path(workspace_path)
    if normalized_path is None:
        return None
    return normalized_path / "ldraw"


def create_workspace_folders(
    workspace_path: str | Path | None,
) -> WorkspaceCreationResult:
    """Create the expected LEGO Builder workspace folders."""
    normalized_path = normalize_optional_path(workspace_path)
    if normalized_path is None:
        return WorkspaceCreationResult(
            is_success=False,
            message="Set a LEGO Library folder first.",
            path=None,
            created_paths=(),
        )

    if normalized_path.exists() and not normalized_path.is_dir():
        return WorkspaceCreationResult(
            is_success=False,
            message="LEGO Library path is not a directory.",
            path=normalized_path,
            created_paths=(),
        )

    created_paths: list[Path] = []
    try:
        if not normalized_path.exists():
            normalized_path.mkdir(parents=True)
            created_paths.append(normalized_path)

        for relative_path in WORKSPACE_DIRECTORIES:
            directory = normalized_path / relative_path
            if not directory.exists():
                directory.mkdir(parents=True)
                created_paths.append(directory)
            elif not directory.is_dir():
                return WorkspaceCreationResult(
                    is_success=False,
                    message=f"LEGO Library item is not a directory: {relative_path}",
                    path=normalized_path,
                    created_paths=tuple(created_paths),
                )

        config_path = get_workspace_config_path(normalized_path)
        if config_path.exists():
            if read_workspace_config(normalized_path) is None:
                return WorkspaceCreationResult(
                    is_success=False,
                    message="LEGO Library marker config is invalid.",
                    path=normalized_path,
                    created_paths=tuple(created_paths),
                )
        elif has_valid_legacy_workspace_config(normalized_path):
            write_workspace_config(normalized_path)
            created_paths.append(config_path)
        else:
            write_workspace_config(normalized_path)
            created_paths.append(config_path)
    except OSError as error:
        return WorkspaceCreationResult(
            is_success=False,
            message=f"Could not create LEGO Library folders: {error}",
            path=normalized_path,
            created_paths=tuple(created_paths),
        )

    return WorkspaceCreationResult(
        is_success=True,
        message="LEGO Library folders are ready.",
        path=normalized_path,
        created_paths=tuple(created_paths),
    )
