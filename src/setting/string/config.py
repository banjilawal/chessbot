# src/setting/string/config.py

"""
Module: setting.string.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

__all__ = [
    "MIN_LENGTH",
    "MAX_LENGTH",
    "StringPropertyTable",
]

from setting import StringProperty

MIN_LENGTH = 2
MAX_LENGTH = 40


@dataclass
class StringPropertyTable:
    """
    Role
        -   Property Settings
  
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