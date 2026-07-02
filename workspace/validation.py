"""Pure Python validation helpers for LEGO Builder workspaces."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

try:
    from ..utils.paths import normalize_optional_path
except ImportError:  # Allows local tests to import this module outside Blender.
    from utils.paths import normalize_optional_path

try:
    from .config import CONFIG_FILENAME, read_workspace_config
    from .structure import WORKSPACE_DIRECTORIES
except ImportError:  # Allows local tests to import this module outside Blender.
    from workspace.config import CONFIG_FILENAME, read_workspace_config
    from workspace.structure import WORKSPACE_DIRECTORIES


@dataclass(frozen=True)
class WorkspaceValidationResult:
    """Validation result for a LEGO Builder workspace path."""

    is_valid: bool
    status: str
    message: str
    path: Path | None
    missing_paths: tuple[Path, ...]

    @property
    def status_label(self) -> str:
        """Return a concise status label for Blender UI display."""
        if self.status == "ready":
            return "LEGO Library: Ready"
        if self.status == "not_configured":
            return "LEGO Library: Not configured"
        if self.status == "missing":
            return "LEGO Library: Missing"
        if self.status == "incomplete":
            return "LEGO Library: Incomplete"
        return "LEGO Library: Invalid"


def validate_workspace_path(
    path: str | Path | None,
) -> WorkspaceValidationResult:
    """Validate whether a path is a complete LEGO Builder workspace."""
    normalized_path = normalize_optional_path(path)

    if normalized_path is None:
        return WorkspaceValidationResult(
            is_valid=False,
            status="not_configured",
            message="Set a LEGO Library folder in add-on preferences.",
            path=None,
            missing_paths=(),
        )

    if not normalized_path.exists():
        return WorkspaceValidationResult(
            is_valid=False,
            status="missing",
            message="Create LEGO Library folders to initialize this location.",
            path=normalized_path,
            missing_paths=(),
        )

    if not normalized_path.is_dir():
        return WorkspaceValidationResult(
            is_valid=False,
            status="invalid",
            message="LEGO Library path is not a directory.",
            path=normalized_path,
            missing_paths=(),
        )

    missing_paths = tuple(
        relative_path
        for relative_path in WORKSPACE_DIRECTORIES
        if not (normalized_path / relative_path).is_dir()
    )
    config = read_workspace_config(normalized_path)
    if config is None:
        missing_paths += (Path(CONFIG_FILENAME),)

    if missing_paths:
        return WorkspaceValidationResult(
            is_valid=False,
            status="incomplete",
            message="LEGO Library folders or marker config are missing.",
            path=normalized_path,
            missing_paths=missing_paths,
        )

    return WorkspaceValidationResult(
        is_valid=True,
        status="ready",
        message="LEGO Library is ready.",
        path=normalized_path,
        missing_paths=(),
    )
