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
    table: Mapping[str, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                "frame_dimension": 800,
                "frame_width": 800,
                "frame_height": 800,
            }
        )
    )