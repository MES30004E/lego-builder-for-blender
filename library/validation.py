"""Pure Python validation helpers for LEGO library paths."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

try:
    from ..utils.paths import normalize_optional_path
except ImportError:  # Allows local tests to import this module outside Blender.
    from utils.paths import normalize_optional_path


@dataclass(frozen=True)
class LDrawLibraryValidationResult:
    """Validation result for a potential LDraw library path."""

    is_valid: bool
    status: str
    message: str
    path: Path | None

    @property
    def status_label(self) -> str:
        """Return a concise status label for Blender UI display."""
        if self.status == "ready":
            return "LDraw library: Ready"
        if self.status == "not_configured":
            return "LDraw library: Not configured"
        return "LDraw library: Invalid path"


def validate_ldraw_library_path(
    path: str | Path | None,
) -> LDrawLibraryValidationResult:
    """Validate whether a path looks like an LDraw library root."""
    normalized_path = normalize_optional_path(path)

    if normalized_path is None:
        return LDrawLibraryValidationResult(
            is_valid=False,
            status="not_configured",
            message="Set an LDraw library path in add-on preferences.",
            path=None,
        )

    if not normalized_path.exists():
        return LDrawLibraryValidationResult(
            is_valid=False,
            status="missing",
            message="Path does not exist.",
            path=normalized_path,
        )

    if not normalized_path.is_dir():
        return LDrawLibraryValidationResult(
            is_valid=False,
            status="not_directory",
            message="Path is not a directory.",
            path=normalized_path,
        )

    missing_markers = [
        marker for marker in ("parts", "p") if not (normalized_path / marker).is_dir()
    ]
    if missing_markers:
        return LDrawLibraryValidationResult(
            is_valid=False,
            status="missing_markers",
            message="Expected parts/ and p/ directories.",
            path=normalized_path,
        )

    return LDrawLibraryValidationResult(
        is_valid=True,
        status="ready",
        message="LDraw library path looks valid.",
        path=normalized_path,
    )
