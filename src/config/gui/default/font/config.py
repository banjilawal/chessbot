# src/config/gui/default/font/config.py

"""
Module: config.gui.default.font.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field



@dataclass
class DefaultFontSetting:
    """
    Role
        -   Configuration Settings

    Responsibilities:
        1.  Default frame size.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[str, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                "font": 800,
                "width": 800,
                "height": 800,
            }
        )
    )
    PYGAME_FONT = "monospace"
    PYGAME_FONT_SIZE = 150