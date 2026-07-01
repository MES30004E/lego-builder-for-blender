"""Pure Python in-memory indexing for LDraw part libraries."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

try:
    from .metadata import LDrawPartMetadata, extract_part_metadata
    from .validation import validate_ldraw_library_path
except ImportError:  # Allows local tests to import this module outside Blender.
    from library.metadata import LDrawPartMetadata, extract_part_metadata
    from library.validation import validate_ldraw_library_path


@dataclass(frozen=True)
class LDrawPartIndex:
    """In-memory index of basic LDraw part metadata."""

    library_path: Path
    parts: tuple[LDrawPartMetadata, ...]

    @property
    def part_count(self) -> int:
        """Return the number of indexed parts."""
        return len(self.parts)


@dataclass(frozen=True)
class LDrawIndexBuildResult:
    """Result of an LDraw part index build."""

    is_success: bool
    message: str
    index: LDrawPartIndex | None


_current_index: LDrawPartIndex | None = None


def build_ldraw_part_index(library_path: str | Path | None) -> LDrawIndexBuildResult:
    """Build an in-memory index for an LDraw library's parts directory."""
    validation_result = validate_ldraw_library_path(library_path)
    if not validation_result.is_valid or validation_result.path is None:
        return LDrawIndexBuildResult(
            is_success=False,
            message=validation_result.message,
            index=None,
        )

    root_path = validation_result.path
    part_files = sorted(
        (root_path / "parts").rglob("*.dat"),
        key=lambda file_path: file_path.relative_to(root_path).as_posix().lower(),
    )
    parts = tuple(
        extract_part_metadata(file_path, root_path) for file_path in part_files
    )
    index = LDrawPartIndex(library_path=root_path, parts=parts)

    return LDrawIndexBuildResult(
        is_success=True,
        message=f"Indexed {index.part_count:,} parts.",
        index=index,
    )


def set_current_index(index: LDrawPartIndex | None) -> None:
    """Set the active in-memory part index."""
    global _current_index

    _current_index = index


def get_current_index() -> LDrawPartIndex | None:
    """Return the active in-memory part index, if one exists."""
    return _current_index


def clear_current_index() -> None:
    """Clear the active in-memory part index."""
    set_current_index(None)
