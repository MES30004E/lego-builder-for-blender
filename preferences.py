"""Add-on preferences for LEGO Builder for Blender."""

from __future__ import annotations

import bpy
from bpy.props import BoolProperty, StringProperty
from bpy.types import AddonPreferences

from .library.index import get_current_index
from .library.validation import validate_ldraw_library_path
from .workspace.validation import validate_workspace_path

ADDON_PACKAGE = __package__ or __name__.partition(".")[0]


class LEGOBuilderPreferences(AddonPreferences):
    """User preferences for LEGO Builder for Blender."""

    bl_idname = ADDON_PACKAGE

    ldraw_library_path: StringProperty(
        name="LDraw Library Path",
        subtype="DIR_PATH",
        description="Path to the root of an LDraw-compatible parts library",
    )
    workspace_path: StringProperty(
        name="LEGO Library Folder",
        subtype="DIR_PATH",
        description="Path to the LEGO Library folder managed by LEGO Builder",
    )
    show_workspace_settings: BoolProperty(
        name="LEGO Library",
        default=True,
        description="Show LEGO Library settings",
    )
    show_ldraw_settings: BoolProperty(
        name="LDraw",
        default=True,
        description="Show LDraw library settings",
    )
    show_help_settings: BoolProperty(
        name="Help",
        default=False,
        description="Show LEGO Builder help links",
    )

    def draw(self, context: bpy.types.Context) -> None:
        """Draw the add-on preferences UI."""
        del context

        layout = self.layout
        _draw_workspace_section(layout, self)
        _draw_ldraw_section(layout, self)
        _draw_help_section(layout, self)


def _draw_workspace_section(
    layout: bpy.types.UILayout,
    prefs: LEGOBuilderPreferences,
) -> None:
    """Draw collapsible LEGO Library preferences."""
    box = layout.box()
    is_open = prefs.show_workspace_settings
    icon = "TRIA_DOWN" if is_open else "TRIA_RIGHT"
    row = box.row()
    row.prop(
        prefs,
        "show_workspace_settings",
        text="LEGO Library",
        icon=icon,
        emboss=False,
    )
    if not is_open:
        return

    box.prop(prefs, "workspace_path")
    workspace_result = validate_workspace_path(prefs.workspace_path)
    workspace_icon = "CHECKMARK" if workspace_result.is_valid else "ERROR"
    box.label(text=workspace_result.status_label, icon=workspace_icon)
    if workspace_result.message:
        box.label(text=workspace_result.message)

    actions = box.row(align=True)
    actions.operator(
        "lego_builder.create_workspace_folders",
        text="Create LEGO Library",
    )
    actions.operator("lego_builder.open_workspace_folder", text="Open LEGO Library")


def _draw_ldraw_section(
    layout: bpy.types.UILayout,
    prefs: LEGOBuilderPreferences,
) -> None:
    """Draw collapsible LDraw preferences."""
    box = layout.box()
    is_open = prefs.show_ldraw_settings
    icon = "TRIA_DOWN" if is_open else "TRIA_RIGHT"
    row = box.row()
    row.prop(
        prefs,
        "show_ldraw_settings",
        text="LDraw",
        icon=icon,
        emboss=False,
    )
    if not is_open:
        return

    box.prop(prefs, "ldraw_library_path")
    box.operator(
        "lego_builder.use_workspace_ldraw_library",
        text="Use LEGO Library LDraw",
    )

    ldraw_result = validate_ldraw_library_path(prefs.ldraw_library_path)
    ldraw_icon = "CHECKMARK" if ldraw_result.is_valid else "ERROR"
    box.label(text=ldraw_result.status_label, icon=ldraw_icon)
    if ldraw_result.message:
        box.label(text=ldraw_result.message)

    box.label(text=_part_index_status(prefs.ldraw_library_path))
    box.operator("lego_builder.build_part_index", text="Refresh Library")


def _draw_help_section(
    layout: bpy.types.UILayout,
    prefs: LEGOBuilderPreferences,
) -> None:
    """Draw collapsible help links."""
    box = layout.box()
    is_open = prefs.show_help_settings
    icon = "TRIA_DOWN" if is_open else "TRIA_RIGHT"
    row = box.row()
    row.prop(
        prefs,
        "show_help_settings",
        text="Help",
        icon=icon,
        emboss=False,
    )
    if not is_open:
        return

    row = box.row(align=True)
    row.operator("lego_builder.open_documentation", text="Documentation")
    row.operator("lego_builder.open_github", text="GitHub")


def _part_index_status(path: str | None) -> str:
    """Return a concise indexed-parts status for preferences."""
    current_index = get_current_index()
    if current_index is None:
        return "Indexed Parts: Not built"

    if str(current_index.library_path) != str(validate_ldraw_library_path(path).path):
        return "Indexed Parts: Needs refresh"

    return f"Indexed Parts: {current_index.part_count:,}"


def get_preferences(context: bpy.types.Context) -> LEGOBuilderPreferences | None:
    """Return add-on preferences for the active extension package."""
    addon = context.preferences.addons.get(ADDON_PACKAGE)
    if addon is None:
        return None
    preferences = addon.preferences
    if isinstance(preferences, LEGOBuilderPreferences):
        return preferences
    return None
