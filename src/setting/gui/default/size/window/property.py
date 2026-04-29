# src/setting/gui/default/size/setting/window/property.py

"""
Module: setting.gui.default.size.setting.window.property
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class WindowProperty(Enum):
    FRAME_DIMENSION = auto(),
    FRAME_WIDTH = auto(),
    FRAME_HEIGHT = auto(),