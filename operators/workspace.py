"""Operators for managing the LEGO Builder workspace."""

from __future__ import annotations

import bpy
from bpy.types import Operator

from ..preferences import get_preferences
from ..runtime.state import set_current_library, set_current_workspace
from ..workspace.structure import create_workspace_folders, get_workspace_ldraw_path
from ..workspace.validation import validate_workspace_path


class LEGO_BUILDER_OT_create_workspace_folders(Operator):
    """Create the expected LEGO Builder workspace folders."""

    bl_idname = "lego_builder.create_workspace_folders"
    bl_label = "Create LEGO Library"
    bl_description = "Create the LEGO Library folder structure"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Create library folders from the configured workspace path."""
        preferences = get_preferences(context)
        if preferences is None:
            self.report({"ERROR"}, "LEGO Builder preferences are unavailable.")
            return {"CANCELLED"}

        result = create_workspace_folders(preferences.workspace_path)
        if not result.is_success:
            self.report({"ERROR"}, result.message)
            return {"CANCELLED"}

        set_current_workspace(result.path)
        self.report({"INFO"}, result.message)
        return {"FINISHED"}


class LEGO_BUILDER_OT_open_workspace_folder(Operator):
    """Open the configured workspace folder."""

    bl_idname = "lego_builder.open_workspace_folder"
    bl_label = "Open LEGO Library"
    bl_description = "Open the LEGO Library folder"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Open the configured workspace folder using Blender."""
        preferences = get_preferences(context)
        if preferences is None:
            self.report({"ERROR"}, "LEGO Builder preferences are unavailable.")
            return {"CANCELLED"}

        result = validate_workspace_path(preferences.workspace_path)
        if result.path is None or not result.path.exists() or not result.path.is_dir():
            self.report({"ERROR"}, "LEGO Library folder is not available.")
            return {"CANCELLED"}

        try:
            bpy.ops.wm.path_open(filepath=str(result.path))
        except (AttributeError, RuntimeError, TypeError, ValueError):
            self.report({"WARNING"}, "Could not open the LEGO Library folder.")
            return {"CANCELLED"}

        self.report({"INFO"}, "Opened LEGO Library folder.")
        return {"FINISHED"}


class LEGO_BUILDER_OT_use_workspace_ldraw_library(Operator):
    """Use the workspace LDraw folder as the configured library path."""

    bl_idname = "lego_builder.use_workspace_ldraw_library"
    bl_label = "Use LEGO Library LDraw"
    bl_description = "Set the LDraw library path to the LEGO Library ldraw folder"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Point the LDraw library preference at the workspace ldraw folder."""
        preferences = get_preferences(context)
        if preferences is None:
            self.report({"ERROR"}, "LEGO Builder preferences are unavailable.")
            return {"CANCELLED"}

        workspace_result = validate_workspace_path(preferences.workspace_path)
        if not workspace_result.is_valid:
            self.report({"ERROR"}, workspace_result.message)
            return {"CANCELLED"}

        set_current_workspace(workspace_result.path)
        ldraw_path = get_workspace_ldraw_path(workspace_result.path)
        if ldraw_path is None:
            self.report({"ERROR"}, "LEGO Library LDraw folder is unavailable.")
            return {"CANCELLED"}

        preferences.ldraw_library_path = str(ldraw_path)
        set_current_library(ldraw_path)
        self.report({"INFO"}, "Using LEGO Library LDraw.")
        return {"FINISHED"}
