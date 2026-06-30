"""LEGO Builder for Blender add-on entry point."""

from __future__ import annotations

import bpy
from bpy.types import Panel

bl_info = {
    "name": "LEGO Builder for Blender",
    "author": "LEGO Builder for Blender contributors",
    "version": (0, 1, 0),
    "blender": (5, 1, 0),
    "location": "View3D > Sidebar > LEGO",
    "description": "A Blender-native LEGO building environment.",
    "category": "3D View",
}


class LEGO_BUILDER_PT_main_panel(Panel):
    """Main sidebar panel for the LEGO Builder add-on."""

    bl_label = "LEGO Builder"
    bl_idname = "LEGO_BUILDER_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LEGO"

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the panel contents."""
        del context

        layout = self.layout
        layout.label(text="LEGO Builder is working!")


classes = (LEGO_BUILDER_PT_main_panel,)


def register() -> None:
    """Register the add-on classes with Blender."""
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister() -> None:
    """Unregister the add-on classes from Blender."""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
