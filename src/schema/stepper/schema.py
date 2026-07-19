# src/schema/terminus/schema.py

"""
Module: schema.terminus.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum

import setting
from model import Vector


class QuadrantStepFunction(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set


    Responsibilities:
        1.  Terminus of each quadrant

    Attributes:
        orientation: str
        x_step: int
        slope: int

    Super Class:
        Enum
    """
    
    def __new__(
            cls,
            orientation: str,
            x_step: int,
            slope: int
    ):
        """
        Args:
            orientation: str
            x_step: int
            slope: int
        """
        obj = object.__new__(cls)
        obj._orientation = orientation
        obj._x_step = x_step
        obj._slope = slope
        return obj
    
    NORTHWEST = ("northwest", -1, -1)
    NORTHEAST = ("northeast", 1, -1)
    SOUTHEAST = ("southeast", 1, 1)
    SOUTHWEST = ("southwest", -1, 1)
    
    @property
    def orientation(self) -> str:
        return self._orientation
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope



 