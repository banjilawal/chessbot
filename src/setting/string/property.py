# src/setting/string/property.py

"""
Module: setting.string.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto

__all__ = [
    "StringProperty",
]
class StringProperty(Enum):
    MIN_LENGTH = auto(),
    MAX_LENGTH = auto(),