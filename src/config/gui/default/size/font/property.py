# src/config/gui/default/size/config/font/property.py

"""
Module: config.gui.default.size.config.font.property
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class TextFunctionProperty(Enum):
    TITLE = auto(),
    MENU_HEADING = auto(),
    STANDARD = auto(),
    CAPTION = auto(),
    NOTIFICATION = auto(),