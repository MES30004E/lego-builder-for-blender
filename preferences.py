"""Add-on preferences for LEGO Builder for Blender."""

import bpy
from bpy.props import StringProperty
from bpy.types import AddonPreferences

from .library.validation import validate_ldraw_library_path

ADDON_PACKAGE = __package__ or __name__.partition(".")[0]


class LEGOBuilderPreferences(AddonPreferences):
    """User preferences for LEGO Builder for Blender."""

    bl_idname = ADDON_PACKAGE

    ldraw_library_path: StringProperty(
        name="LDraw Library Path",
        subtype="DIR_PATH",
        description="Path to the root of an LDraw-compatible parts library",
    )

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the add-on preferences UI."""
        del context

        layout = self.layout
        layout.prop(self, "ldraw_library_path")

        result = validate_ldraw_library_path(self.ldraw_library_path)
        icon = "CHECKMARK" if result.is_valid else "ERROR"
        layout.label(text=result.status_label, icon=icon)
        if result.message:
            layout.label(text=result.message)


def get_preferences(context: bpy.types.Context) -> LEGOBuilderPreferences | None:
    """Return add-on preferences for the active extension package."""
    addon = context.preferences.addons.get(ADDON_PACKAGE)
    if addon is None:
        return None
    preferences = addon.preferences
    if isinstance(preferences, LEGOBuilderPreferences):
        return preferences
    return None
