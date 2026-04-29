# src/setting/gui/default/font/setting.py

"""
Module: setting.gui.default.font.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from setting import FontProperty


@dataclass
class FontPropertyTable:
    """
    Role
        -   Property Settings

    Responsibilities:
        1.  Default frame size.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[FontProperty, str] = field(
        default_factory=lambda: MappingProxyType(
            {
                FontProperty.DEFAULT: "monospace",
            }
        )
    )