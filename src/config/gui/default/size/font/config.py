# src/config/gui/default/size/config/font/config.py

"""
Module: config.gui.default.size.config.font.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field



@dataclass
class DefaultFontSizeSetting:
    """
    Role
        -   Configuration Settings

    Responsibilities:
        1.  Default font size settings..

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[str, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                "title": 200,
                "menu_heading": 180,
                "standard": 150,
                "caption": 120,
            }
        )
    )