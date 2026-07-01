"""Sidebar panels for LEGO Builder for Blender."""

from __future__ import annotations

import bpy
from bpy.types import Panel

from ..library.index import get_current_index
from ..library.validation import validate_ldraw_library_path
from ..preferences import get_preferences


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
        header.label(text="LEGO Builder is working!")
        header.operator(
            "lego_builder.open_preferences",
            text="",
            icon="PREFERENCES",
        )

        preferences = get_preferences(context)
        path = preferences.ldraw_library_path if preferences else None
        result = validate_ldraw_library_path(path)

        icon = "CHECKMARK" if result.is_valid else "ERROR"
        layout.separator()
        layout.label(text=result.status_label, icon=icon)

        if result.is_valid:
            layout.operator(
                "lego_builder.build_part_index",
                text="Build/Refresh Part Index",
            )
            layout.label(text=_part_index_status(path))


def _part_index_status(path: str | None) -> str:
    """Return a concise part index status for the sidebar."""
    current_index = get_current_index()
    if current_index is None:
        return "Part index: Not built"

    if str(current_index.library_path) != str(validate_ldraw_library_path(path).path):
        return "Part index: Needs refresh"

    return f"Indexed parts: {current_index.part_count:,}"
