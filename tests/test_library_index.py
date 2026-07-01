"""Tests for pure LDraw library indexing."""

from __future__ import annotations

from pathlib import Path

from library.index import build_ldraw_part_index, clear_current_index
from library.index import get_current_index, set_current_index
from library.metadata import extract_part_metadata


def _create_library(root: Path) -> Path:
    """Create a minimal fake LDraw library."""
    (root / "parts").mkdir()
    (root / "p").mkdir()
    return root


def test_unconfigured_library_returns_failed_result() -> None:
    """An unconfigured library cannot be indexed."""
    result = build_ldraw_part_index(None)

    assert not result.is_success
    assert result.index is None


def test_invalid_library_returns_failed_result(tmp_path: Path) -> None:
    """An invalid library cannot be indexed."""
    result = build_ldraw_part_index(tmp_path)

    assert not result.is_success
    assert result.index is None


def test_empty_parts_directory_returns_empty_index(tmp_path: Path) -> None:
    """A valid library with no part files should produce an empty index."""
    library_root = _create_library(tmp_path)

    result = build_ldraw_part_index(library_root)

    assert result.is_success
    assert result.index is not None
    assert result.index.part_count == 0


def test_one_dat_file_indexes_one_part(tmp_path: Path) -> None:
    """A single .dat file should produce one metadata record."""
    library_root = _create_library(tmp_path)
    part_file = library_root / "parts" / "3001.dat"
    part_file.write_text("0 Brick 2 x 4\n", encoding="utf-8")

    result = build_ldraw_part_index(library_root)

    assert result.index is not None
    assert result.index.part_count == 1
    part = result.index.parts[0]
    assert part.part_number == "3001"
    assert part.filename == "3001.dat"
    assert part.display_name == "Brick 2 x 4"
    assert part.relative_path == Path("parts/3001.dat")


def test_nested_dat_files_are_indexed(tmp_path: Path) -> None:
    """Nested .dat files under parts/ should be indexed."""
    library_root = _create_library(tmp_path)
    nested_dir = library_root / "parts" / "s"
    nested_dir.mkdir()
    (nested_dir / "3001s01.dat").write_text("0 Subpart\n", encoding="utf-8")

    result = build_ldraw_part_index(library_root)

    assert result.index is not None
    assert result.index.part_count == 1
    assert result.index.parts[0].relative_path == Path("parts/s/3001s01.dat")


def test_non_dat_files_are_ignored(tmp_path: Path) -> None:
    """Only .dat files should be indexed."""
    library_root = _create_library(tmp_path)
    (library_root / "parts" / "readme.txt").write_text("ignore", encoding="utf-8")

    result = build_ldraw_part_index(library_root)

    assert result.index is not None
    assert result.index.part_count == 0


def test_metadata_lines_are_skipped_for_display_name(tmp_path: Path) -> None:
    """LDraw metadata comments should not become display names."""
    library_root = _create_library(tmp_path)
    part_file = library_root / "parts" / "3002.dat"
    part_file.write_text(
        "0 !LDRAW_ORG Part\n0 Name: 3002.dat\n0 Brick 2 x 3\n",
        encoding="utf-8",
    )

    part = extract_part_metadata(part_file, library_root)

    assert part.display_name == "Brick 2 x 3"


def test_missing_display_name_falls_back_to_part_number(tmp_path: Path) -> None:
    """A part without meaningful comments should use its part number."""
    library_root = _create_library(tmp_path)
    part_file = library_root / "parts" / "3003.dat"
    part_file.write_text("1 16 0 0 0 1 0 0 0 1 0 0 0 1 box.dat\n", encoding="utf-8")

    part = extract_part_metadata(part_file, library_root)

    assert part.display_name == "3003"


def test_index_ordering_is_deterministic(tmp_path: Path) -> None:
    """Indexed parts should be sorted by relative path."""
    library_root = _create_library(tmp_path)
    (library_root / "parts" / "b.dat").write_text("0 B\n", encoding="utf-8")
    (library_root / "parts" / "a.dat").write_text("0 A\n", encoding="utf-8")

    result = build_ldraw_part_index(library_root)

    assert result.index is not None
    assert [part.filename for part in result.index.parts] == ["a.dat", "b.dat"]


def test_current_index_state_can_be_set_and_cleared(tmp_path: Path) -> None:
    """The in-memory index should be explicitly replaceable and clearable."""
    library_root = _create_library(tmp_path)
    result = build_ldraw_part_index(library_root)
    assert result.index is not None

    set_current_index(result.index)
    assert get_current_index() == result.index

    clear_current_index()
    assert get_current_index() is None
