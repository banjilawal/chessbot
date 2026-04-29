# src/setting/name/property.py

"""
Module: setting.name.property
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum, auto


class NameProperty(Enum):
    MIN_LENGTH = auto(),
    MAX_LENGTH = auto(),