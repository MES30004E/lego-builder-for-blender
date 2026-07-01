"""Metadata extraction for LDraw part files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

_SKIPPED_COMMENT_PREFIXES = (
    "!",
    "//",
    "NAME:",
    "AUTHOR:",
    "BFC",
    "CATEGORY",
    "KEYWORDS",
    "LICENSE",
    "HELP",
    "HISTORY",
    "CMDLINE",
)


@dataclass(frozen=True)
class LDrawPartMetadata:
    """Basic catalog metadata for one LDraw part file."""

    part_number: str
    filename: str
    display_name: str
    relative_path: Path


def extract_part_metadata(file_path: Path, library_root: Path) -> LDrawPartMetadata:
    """Extract basic metadata from an LDraw part file."""
    part_number = file_path.stem
    display_name = _extract_display_name(file_path) or part_number

    return LDrawPartMetadata(
        part_number=part_number,
        filename=file_path.name,
        display_name=display_name,
        relative_path=file_path.relative_to(library_root),
    )


def _extract_display_name(file_path: Path) -> str | None:
    """Return the first meaningful LDraw comment line from a part file."""
    with file_path.open("r", encoding="utf-8", errors="replace") as part_file:
        for line in part_file:
            stripped_line = line.strip()
            if not stripped_line.startswith("0"):
                continue

            comment = stripped_line[1:].strip()
            if _is_meaningful_display_comment(comment):
                return comment

    return None


def _is_meaningful_display_comment(comment: str) -> bool:
    """Return whether a comment is suitable as a display name."""
    if not comment:
        return False

    normalized_comment = comment.upper()
    return not normalized_comment.startswith(_SKIPPED_COMMENT_PREFIXES)
