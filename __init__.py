"""LEGO Builder for Blender add-on entry point."""

from __future__ import annotations

from . import registration as _registration

bl_info = {
    "name": "LEGO Builder for Blender",
    "author": "MES30004E",
    "version": (0, 3, 0),
    "blender": (5, 1, 0),
    "location": "View3D > Sidebar > LEGO",
    "description": "A Blender-native LEGO building environment.",
    "category": "3D View",
}


def register() -> None:
    """Register the add-on with Blender."""
    _registration.register()


def unregister() -> None:
    """Unregister the add-on from Blender."""
    _registration.unregister()
