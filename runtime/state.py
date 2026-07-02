"""In-memory runtime state for LEGO Builder for Blender."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    try:
        from ..library.index import LDrawPartIndex
    except ImportError:
        from library.index import LDrawPartIndex

_current_workspace: Path | None = None
_current_library: Path | None = None
_current_index: LDrawPartIndex | None = None


def set_current_workspace(path: Path | None) -> None:
    """Set the active workspace path for this Blender session."""
    global _current_workspace

    _current_workspace = path


def get_current_workspace() -> Path | None:
    """Return the active workspace path for this Blender session."""
    return _current_workspace


def set_current_library(path: Path | None) -> None:
    """Set the active LDraw library path for this Blender session."""
    global _current_library

    _current_library = path


def get_current_library() -> Path | None:
    """Return the active LDraw library path for this Blender session."""
    return _current_library


def set_current_index(index: LDrawPartIndex | None) -> None:
    """Set the active in-memory part index."""
    global _current_index

    _current_index = index
    set_current_library(index.library_path if index is not None else None)


def get_current_index() -> LDrawPartIndex | None:
    """Return the active in-memory part index, if one exists."""
    return _current_index


def clear_current_index() -> None:
    """Clear the active in-memory part index."""
    set_current_index(None)
