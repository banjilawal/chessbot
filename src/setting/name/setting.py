# src/setting/name/setting.py

"""
Module: setting.name.setting
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field

from setting import NameProperty


@dataclass
class NameSetting:
    """
    Role
        -   Property Settings
  
    Responsibilities:
        1.  Default colors of name elements.
  
    Attributes:
  
    Provides:
  
    Super Class:
        Enum
    """
    table: Mapping[NameProperty, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                MIN_NAME_LENGTH: 2,
                MAX_NAME_LENGTH: 40,
            }
        )
    )