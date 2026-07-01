"""Operators for building the in-memory LDraw part index."""

from __future__ import annotations

import bpy
from bpy.types import Operator

from ..library.index import (
    build_ldraw_part_index,
    clear_current_index,
    set_current_index,
)
from ..preferences import get_preferences


class LEGO_BUILDER_OT_build_part_index(Operator):
    """Build or refresh the in-memory LDraw part index."""

    bl_idname = "lego_builder.build_part_index"
    bl_label = "Build/Refresh Part Index"
    bl_description = "Build an in-memory index of LDraw .dat files"

    def execute(self, context: bpy.types.Context) -> set[str]:
        """Build the part index from the configured LDraw library path."""
        preferences = get_preferences(context)
        if preferences is None:
            clear_current_index()
            self.report({"ERROR"}, "LEGO Builder preferences are unavailable.")
            return {"CANCELLED"}

        result = build_ldraw_part_index(preferences.ldraw_library_path)
        if not result.is_success or result.index is None:
            clear_current_index()
            self.report({"ERROR"}, result.message)
            return {"CANCELLED"}

        set_current_index(result.index)
        self.report({"INFO"}, result.message)
        return {"FINISHED"}
