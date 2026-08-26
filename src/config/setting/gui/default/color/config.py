# src/config/setting/gui/default/color/setting.py

"""
Module: config.setting.gui.default.color.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Mapping, Tuple
from types import MappingProxyType
from dataclasses import dataclass, field


from config.setting import GameColor

@dataclass
class DefaultGameColorSetting:
    """
    Role
        -  Property Settings

    Responsibilities:
        1.  Default colors of board elements.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[str, Tuple] = field(
        default_factory=lambda: MappingProxyType(
            {
                "background": GameColor.DARK_GRAY_1.value,
                "opening_player": GameColor.IVORY.value,
                "following_player": GameColor.BLACK.value,
                "square": GameColor.LIGHT_SAND.value,
                "adjacent_square": GameColor.DARK_GRAY_1.value,
            }
        )
    )