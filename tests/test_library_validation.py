"""Tests for pure LDraw library path validation."""

from __future__ import annotations

from pathlib import Path

from library.validation import validate_ldraw_library_path
from utils.paths import normalize_optional_path


def test_none_path_is_not_configured() -> None:
    """None should be treated as an unconfigured path."""
    result = validate_ldraw_library_path(None)

    assert not result.is_valid
    assert result.status == "not_configured"
    assert result.path is None


def test_empty_path_is_not_configured() -> None:
    """An empty path should be treated as unconfigured."""
    result = validate_ldraw_library_path("")

    assert not result.is_valid
    assert result.status == "not_configured"


def test_whitespace_path_is_not_configured() -> None:
    """Whitespace-only paths should be treated as unconfigured."""
    result = validate_ldraw_library_path("   ")

    assert not result.is_valid
    assert result.status == "not_configured"


def test_missing_path_is_invalid(tmp_path: Path) -> None:
    """A missing path should be invalid."""
    result = validate_ldraw_library_path(tmp_path / "missing")

    assert not result.is_valid
    assert result.status == "missing"


def test_file_path_is_invalid(tmp_path: Path) -> None:
    """A file path should be invalid."""
    file_path = tmp_path / "file.dat"
    file_path.write_text("0 test\n", encoding="utf-8")

    result = validate_ldraw_library_path(file_path)

    assert not result.is_valid
    assert result.status == "not_directory"


def test_directory_without_ldraw_markers_is_invalid(tmp_path: Path) -> None:
    """A directory without LDraw markers should be invalid."""
    result = validate_ldraw_library_path(tmp_path)

    assert not result.is_valid
    assert result.status == "missing_markers"


def test_directory_with_only_parts_is_invalid(tmp_path: Path) -> None:
    """A directory with only parts/ should be invalid."""
    (tmp_path / "parts").mkdir()

    result = validate_ldraw_library_path(tmp_path)

    assert not result.is_valid
    assert result.status == "missing_markers"


def test_directory_with_only_p_is_invalid(tmp_path: Path) -> None:
    """A directory with only p/ should be invalid."""
    (tmp_path / "p").mkdir()

    result = validate_ldraw_library_path(tmp_path)

    assert not result.is_valid
    assert result.status == "missing_markers"


def test_directory_with_parts_and_p_is_valid(tmp_path: Path) -> None:
    """A directory with parts/ and p/ should look like an LDraw library."""
    (tmp_path / "parts").mkdir()
    (tmp_path / "p").mkdir()

    result = validate_ldraw_library_path(tmp_path)

    assert result.is_valid
    assert result.status == "ready"
    assert result.path == tmp_path


def test_normalize_optional_path_expands_home() -> None:
    """The public path helper should expand user home paths."""
    result = normalize_optional_path("~/ldraw")

    assert result is not None
    assert not str(result).startswith("~")
