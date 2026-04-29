# src/config/gui/default/size/config/window/property.py

"""
Module: config.gui.default.size.config.window.property
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