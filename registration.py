"""Central Blender class registration for LEGO Builder for Blender."""

from __future__ import annotations

import bpy

from .operators.index_library import LEGO_BUILDER_OT_build_part_index
from .operators.preferences import (
    LEGO_BUILDER_OT_open_documentation,
    LEGO_BUILDER_OT_open_github,
    LEGO_BUILDER_OT_open_preferences,
)
from .operators.workspace import (
    LEGO_BUILDER_OT_create_workspace_folders,
    LEGO_BUILDER_OT_open_workspace_folder,
    LEGO_BUILDER_OT_use_workspace_ldraw_library,
)
from .preferences import LEGOBuilderPreferences
from .ui.panels import LEGO_BUILDER_PT_main_panel

CLASSES = (
    LEGOBuilderPreferences,
    LEGO_BUILDER_OT_build_part_index,
    LEGO_BUILDER_OT_open_preferences,
    LEGO_BUILDER_OT_open_documentation,
    LEGO_BUILDER_OT_open_github,
    LEGO_BUILDER_OT_create_workspace_folders,
    LEGO_BUILDER_OT_open_workspace_folder,
    LEGO_BUILDER_OT_use_workspace_ldraw_library,
    LEGO_BUILDER_PT_main_panel,
)

_registered_classes: list[type] = []


def register() -> None:
    """Register all Blender classes in dependency order."""
    registered_this_call: list[type] = []

    try:
        for cls in CLASSES:
            bpy.utils.register_class(cls)
            _registered_classes.append(cls)
            registered_this_call.append(cls)
    except Exception:
        for cls in reversed(registered_this_call):
            _unregister_class_safely(cls)
            if cls in _registered_classes:
                _registered_classes.remove(cls)
        raise


def unregister() -> None:
    """Unregister Blender classes in reverse registration order."""
    while _registered_classes:
        cls = _registered_classes.pop()
        _unregister_class_safely(cls)


def _unregister_class_safely(cls: type) -> None:
    """Unregister a Blender class, tolerating development reload state."""
    try:
        bpy.utils.unregister_class(cls)
    except (RuntimeError, ValueError):
        return
