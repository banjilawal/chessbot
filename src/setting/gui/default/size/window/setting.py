# src/setting/gui/default/size/setting/window/setting.py

"""
Module: setting.gui.default.size.setting.window.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from setting.gui.default.size.window.property import WindowProperty


@dataclass
class DefaultWindowSizeSetting:
    """
    Role
        -   Property Settings

    Responsibilities:
        1.  Default window size.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[WindowProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                WindowProperty.FRAME_DIMENSION: 800,
                WindowProperty.FRAME_HEIGHT: 800,
                WindowProperty.FRAME_WIDTH: 800,
            }
        )
    )