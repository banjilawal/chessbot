# src/setting/gui/default/size/setting/font/setting.py

"""
Module: setting.gui.default.size.setting.font.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from setting import TextFunctionProperty


@dataclass
class DefaultFontSizeSetting:
    """
    Role
        -   Property Settings

    Responsibilities:
        1.  Default font size settings..

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[TextFunctionProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                TextFunctionProperty.TITLE: 200,
                TextFunctionProperty.MENU_HEADING: 180,
                TextFunctionProperty.DEFAULT: 150,
                TextFunctionProperty.CAPTION: 120,
            }
        )
    )