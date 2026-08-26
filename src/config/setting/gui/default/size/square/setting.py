# src/config/setting/gui/default/size/setting/square/setting.py

"""
Module: config.setting.gui.default.size.setting.square.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from config.setting.gui.default.size.square.property import SquareProperty


@dataclass
class DefaultSquareSizeSetting:
    """
    Role
        -  Property Settings

    Responsibilities:
        1.  Default square pixel size settings.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[SquareProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                SquareProperty.DIMENSION: 80,
                SquareProperty.BORDER_WIDTH: 2,
            }
        )
    )