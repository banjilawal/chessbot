# src/schema/delta/schema.py

"""
Module: schema.delta.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum

import setting
from model import Vector


class AxialDelta(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set


    Responsibilities:
        1.  Vectors for advancing on an axis from the origin to the delta.

    Attributes:
        orientation: str
        vector: Vector

    Super Class:
        Enum
    """
    
    def __new__(
            cls,
            orientation: str,
            vector: Vector,
    ):
        """
        Args:
            orientation: str
            vector: Vector
        """
        obj = object.__new__(cls)
        obj._orientation = orientation
        obj._vector = vector
        return obj
    
    NORTH = ("north", Vector(x=0, y=-1),)
    EAST = ("east", Vector(x=1, y=0),)
    SOUTH = ("south", Vector(x=0, y=1),)
    WEST = ("west", Vector(x=-1, y=0),)
    
    @property
    def orientation(self) -> str:
        return self._orientation
    
    @property
    def vector(self) -> Vector:
        return self._vector