# src/config/gui/default/size/config/frame/config.py

"""
Module: config.gui.default.size.config.frame.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field



@dataclass
class DefaultFrameSizeSetting:
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
                "size": 800,
                "width": 800,
                "height": 800,
            }
        )
    )