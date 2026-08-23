# src/config/setting/gui/default/size/setting/font/property.py

"""
Module: config.setting.gui.default.size.setting.font.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class TextFunctionProperty(Enum):
    TITLE = auto(),
    CAPTION = auto(),
    DEFAULT = auto(),
    NOTIFICATION = auto(),
    MENU_HEADING = auto(),