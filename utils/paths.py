"""Path helpers for LEGO Builder for Blender."""

from __future__ import annotations

from pathlib import Path


def normalize_optional_path(path: str | Path | None) -> Path | None:
    """Normalize an optional user path without requiring it to exist."""
    if path is None:
        return None

    if isinstance(path, Path):
        raw_path = path
    else:
        stripped_path = path.strip()
        if not stripped_path:
            return None
        raw_path = Path(stripped_path)

    if not str(raw_path):
        return None

    return raw_path.expanduser()
