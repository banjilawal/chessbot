# src/config/property/name/numeric/property.py

"""
Module: config.property.name.numeric.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum, auto


class NumericPropertyName(Enum):
    """
     Role:
        1.  Configuration
        2.  Metadata

     Responsibilities:
         1. Names of NumericProperty attribute.

     Attributes:

     Provides:

     Super Class:
        Enum
     """
    MIN_ID = auto(),
    FLOOR = auto(),
    CEILING = auto(),
    INFINITY = auto(),
    NEGATIVE_INFINITY = auto(),


