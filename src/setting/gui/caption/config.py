# src/setting/gui/caption/setting.py

"""
Module: setting.gui.caption.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field


@dataclass
class CaptionTextSetting:
    """
    Role
        -   Property Settings

    Responsibilities:
        1.  Default square pixel size settings.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[str, str] = field(
        default_factory=lambda: MappingProxyType(
            {
                "title": "ChessBot",
                "border_width": 2,
            }
        )
    )