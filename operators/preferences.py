"""Operators for opening LEGO Builder preferences."""

from __future__ import annotations

import bpy
from bpy.types import Operator

from ..preferences import ADDON_PACKAGE


class LEGO_BUILDER_OT_open_preferences(Operator):
    """Open Blender preferences for the LEGO Builder add-on."""

    bl_idname = "lego_builder.open_preferences"
    bl_label = "Preferences"
    bl_description = "Open Blender preferences for LEGO Builder"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Open Blender preferences and try to focus this add-on."""
        del context

        opened_preferences = _open_preferences_window()
        _show_addon_preferences()

        if not opened_preferences:
            self.report({"WARNING"}, "Could not open Blender Preferences.")
            return {"CANCELLED"}

        self.report({"INFO"}, "Opened LEGO Builder preferences.")
        return {"FINISHED"}


def _open_preferences_window() -> bool:
    """Open Blender preferences using the most likely available sections."""
    for section in ("ADDONS", "EXTENSIONS"):
        try:
            bpy.ops.screen.userpref_show("INVOKE_DEFAULT", section=section)
            return True
        except (RuntimeError, TypeError, ValueError):
            continue

    try:
        bpy.ops.screen.userpref_show("INVOKE_DEFAULT")
    except (RuntimeError, TypeError, ValueError):
        return False
    return True


def _show_addon_preferences() -> None:
    """Try to expand this add-on in Blender preferences."""
    try:
        bpy.ops.preferences.addon_show(module=ADDON_PACKAGE)
    except (AttributeError, RuntimeError, TypeError, ValueError):
        return
