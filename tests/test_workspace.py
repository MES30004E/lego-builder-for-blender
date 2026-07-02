"""Tests for pure LEGO Builder workspace logic."""

from __future__ import annotations

from pathlib import Path

from workspace.config import (
    get_legacy_workspace_config_path,
    get_workspace_config_path,
    read_workspace_config,
    write_workspace_config,
)
from workspace.structure import create_workspace_folders, get_workspace_ldraw_path
from workspace.validation import validate_workspace_path


def test_empty_workspace_path_is_not_configured() -> None:
    """An empty workspace path should be treated as unconfigured."""
    result = validate_workspace_path("")

    assert not result.is_valid
    assert result.status == "not_configured"
    assert result.path is None


def test_missing_workspace_path_is_missing(tmp_path: Path) -> None:
    """A missing workspace path should be reported as missing."""
    result = validate_workspace_path(tmp_path / "workspace")

    assert not result.is_valid
    assert result.status == "missing"


def test_file_path_is_invalid(tmp_path: Path) -> None:
    """A file cannot be used as a workspace."""
    file_path = tmp_path / "workspace.txt"
    file_path.write_text("not a directory", encoding="utf-8")

    result = validate_workspace_path(file_path)

    assert not result.is_valid
    assert result.status == "invalid"


def test_empty_existing_directory_is_incomplete(tmp_path: Path) -> None:
    """An empty folder is not yet a complete workspace."""
    result = validate_workspace_path(tmp_path)

    assert not result.is_valid
    assert result.status == "incomplete"
    assert result.missing_paths


def test_partial_workspace_directory_is_incomplete(tmp_path: Path) -> None:
    """A workspace missing required folders should be incomplete."""
    (tmp_path / "ldraw" / "parts").mkdir(parents=True)

    result = validate_workspace_path(tmp_path)

    assert not result.is_valid
    assert result.status == "incomplete"
    assert Path("ldraw/p") in result.missing_paths


def test_create_workspace_from_missing_path(tmp_path: Path) -> None:
    """Workspace creation should initialize a missing root folder."""
    workspace_path = tmp_path / "workspace"

    creation = create_workspace_folders(workspace_path)
    result = validate_workspace_path(workspace_path)

    assert creation.is_success
    assert workspace_path.is_dir()
    assert result.is_valid
    assert result.status == "ready"


def test_create_workspace_from_existing_empty_directory(tmp_path: Path) -> None:
    """Workspace creation should initialize an existing empty folder."""
    creation = create_workspace_folders(tmp_path)
    result = validate_workspace_path(tmp_path)

    assert creation.is_success
    assert result.is_valid
    assert (tmp_path / "cache" / "metadata").is_dir()


def test_marker_config_is_created(tmp_path: Path) -> None:
    """Workspace creation should write a marker config."""
    create_workspace_folders(tmp_path)

    config = read_workspace_config(tmp_path)

    assert config is not None
    assert get_workspace_config_path(tmp_path).is_file()
    assert config.schema_version == 1
    assert config.application == "LEGO Builder"
    assert config.workspace_version == "0.4"
    assert config.created_with == "0.4.0"
    assert config.created_at


def test_complete_workspace_directory_is_ready(tmp_path: Path) -> None:
    """A complete workspace should validate as ready."""
    create_workspace_folders(tmp_path)

    result = validate_workspace_path(tmp_path)

    assert result.is_valid
    assert result.status == "ready"
    assert result.missing_paths == ()


def test_workspace_ldraw_path_is_derived_from_workspace_path(tmp_path: Path) -> None:
    """The workspace LDraw path should be workspace/ldraw."""
    result = get_workspace_ldraw_path(tmp_path)

    assert result == tmp_path / "ldraw"


def test_existing_invalid_marker_config_is_not_overwritten(tmp_path: Path) -> None:
    """Workspace creation should not overwrite an existing marker file."""
    marker_path = get_workspace_config_path(tmp_path)
    marker_path.write_text("not valid toml [", encoding="utf-8")

    creation = create_workspace_folders(tmp_path)

    assert not creation.is_success
    assert marker_path.read_text(encoding="utf-8") == "not valid toml ["


def test_legacy_marker_config_is_recognized(tmp_path: Path) -> None:
    """A valid legacy workspace marker should still validate as ready."""
    create_workspace_folders(tmp_path)
    new_marker = get_workspace_config_path(tmp_path)
    legacy_marker = get_legacy_workspace_config_path(tmp_path)
    legacy_marker.write_text(new_marker.read_text(encoding="utf-8"), encoding="utf-8")
    new_marker.unlink()

    result = validate_workspace_path(tmp_path)

    assert result.is_valid
    assert result.status == "ready"
    assert read_workspace_config(tmp_path) is not None


def test_creation_adds_new_marker_when_legacy_marker_exists(tmp_path: Path) -> None:
    """Creation should preserve a valid legacy marker while adding the new one."""
    create_workspace_folders(tmp_path)
    new_marker = get_workspace_config_path(tmp_path)
    legacy_marker = get_legacy_workspace_config_path(tmp_path)
    legacy_marker.write_text(new_marker.read_text(encoding="utf-8"), encoding="utf-8")
    new_marker.unlink()

    creation = create_workspace_folders(tmp_path)

    assert creation.is_success
    assert new_marker.is_file()
    assert legacy_marker.is_file()


def test_both_marker_configs_are_supported(tmp_path: Path) -> None:
    """A library with both marker configs should validate as ready."""
    create_workspace_folders(tmp_path)
    legacy_marker = get_legacy_workspace_config_path(tmp_path)
    write_workspace_config(tmp_path)
    legacy_marker.write_text(
        get_workspace_config_path(tmp_path).read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    result = validate_workspace_path(tmp_path)

    assert result.is_valid
