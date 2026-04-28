# src/config/gui/default/size/config/square/config.py

"""
Module: config.gui.default.size.config.square.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field



@dataclass
class DefaultSquareSizeSetting:
    """
    Role
        -   Configuration Settings

    Responsibilities:
        1.  Default square pixel size settings.

    Attributes:

    Provides:

    Super Class:
        Enum
    """
    table: Mapping[str, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                "dimension": 80,
                "border_width": 2,
            }
        )
    )