# src/config/setting/string/config.py

"""
Module: config.setting.string.config
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

import sys
from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

__all__ = [
    "StringPropertyTable",
]

from config.setting import StringProperty

MIN_ID = 0
FLOOR = 0
CEILING = 4096
INFINITY = sys.maxsize
NEGATIVE_INFINITY = -1 * INFINITY


@dataclass
class NumericBoundPropertyTable:
    """
    Role
        - Property Settings
  
    Responsibilities:
        1.  Default lengths of Strings.
  
    Attributes:
  
    Provides:
  
    Super Class:
        Enum
    """
    entry: Mapping[StringProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                StringProperty.MIN_LENGTH: MIN_LENGTH,
                StringProperty.MAX_LENGTH: MAX_LENGTH,
            }
        )
    )