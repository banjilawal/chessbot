# src/config/name/config.py

"""
Module: config.name.config
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Mapping
from types import MappingProxyType
from dataclasses import dataclass, field


@dataclass
class NameSetting:
    """
    Role
        -   Configuration Settings
  
    Responsibilities:
        1.  Default colors of name elements.
  
    Attributes:
  
    Provides:
  
    Super Class:
        Enum
    """
    table: Mapping[str, int] = field(
        default_factory=lambda: MappingProxyType(
            {
                "min_length": 2,
                "max_lengths": 40,
            }
        )
    )