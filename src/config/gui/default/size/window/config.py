# src/config/gui/default/size/config/window/config.py

"""
Module: config.gui.default.size.config.window.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from config.gui.default.size.window.property import WindowProperty


@dataclass
class DefaultWindowSizeSetting:
    """
    Role
        -   Configuration Settings

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