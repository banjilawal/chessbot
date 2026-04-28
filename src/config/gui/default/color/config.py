# src/config/gui/default/color/config.py

"""
Module: config.gui.default.color.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping, Tuple
from types import MappingProxyType
from dataclasses import dataclass, field


from config import GameColor

@dataclass
class DefaultGameColorSetting:
    """
    Role
        -   Configuration Settings

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