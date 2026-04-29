# src/setting/gui/default/size/setting/font/property.py

"""
Module: setting.gui.default.size.setting.font.property
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class TextFunctionProperty(Enum):
    TITLE = auto(),
    CAPTION = auto(),
    DEFAULT = auto(),
    NOTIFICATION = auto(),
    MENU_HEADING = auto(),