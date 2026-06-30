"""Sidebar panels for LEGO Builder for Blender."""

from __future__ import annotations

import bpy
from bpy.types import Panel

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
        layout.label(text="LEGO Builder is working!")

        preferences = get_preferences(context)
        path = preferences.ldraw_library_path if preferences else None
        result = validate_ldraw_library_path(path)

        icon = "CHECKMARK" if result.is_valid else "ERROR"
        layout.separator()
        layout.label(text=result.status_label, icon=icon)
