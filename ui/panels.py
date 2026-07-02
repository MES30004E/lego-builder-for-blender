"""Sidebar panels for LEGO Builder for Blender."""

from __future__ import annotations

import bpy
from bpy.types import Panel

from ..library.index import get_current_index
from ..library.validation import validate_ldraw_library_path
from ..preferences import get_preferences
from ..workspace.validation import validate_workspace_path


class LEGO_BUILDER_PT_main_panel(Panel):
    """Main sidebar panel for the LEGO Builder add-on."""

    bl_label = "LEGO Builder"
    bl_idname = "LEGO_BUILDER_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LEGO"

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the panel contents."""
        layout = self.layout
        header = layout.row(align=True)
        header.label(text="LEGO Builder")
        header.operator(
            "lego_builder.open_documentation",
            text="",
            icon="HELP",
        )
        header.operator(
            "lego_builder.open_preferences",
            text="",
            icon="PREFERENCES",
        )

        preferences = get_preferences(context)
        workspace_path = preferences.workspace_path if preferences else None
        workspace_result = validate_workspace_path(workspace_path)
        workspace_icon = "CHECKMARK" if workspace_result.is_valid else "ERROR"

        layout.separator()
        layout.label(text="LEGO Library")
        layout.label(text=_status_text(workspace_result), icon=workspace_icon)
        if not workspace_result.is_valid:
            setup = layout.row(align=True)
            setup.operator(
                "lego_builder.create_workspace_folders",
                text="Create",
            )
            setup.operator(
                "lego_builder.open_preferences",
                text="Settings",
            )

        path = preferences.ldraw_library_path if preferences else None
        result = validate_ldraw_library_path(path)

        icon = "CHECKMARK" if result.is_valid else "ERROR"
        layout.separator()
        layout.label(text="Parts")
        layout.label(text=_status_text(result), icon=icon)
        layout.label(text=_part_index_status(path))

        if result.is_valid:
            layout.operator(
                "lego_builder.build_part_index",
                text="Refresh Library",
            )


def _part_index_status(path: str | None) -> str:
    """Return a concise part index status for the sidebar."""
    current_index = get_current_index()
    if current_index is None:
        return "Indexed: Not built"

    if str(current_index.library_path) != str(validate_ldraw_library_path(path).path):
        return "Indexed: Needs refresh"

    return f"Indexed: {current_index.part_count:,}"


def _status_text(result: object) -> str:
    """Return compact status text without repeating the subject label."""
    status = getattr(result, "status", "")
    if status == "ready":
        return "Ready"
    if status == "not_configured":
        return "Not configured"
    if status == "missing":
        return "Missing"
    if status == "incomplete":
        return "Incomplete"
    return "Invalid"
