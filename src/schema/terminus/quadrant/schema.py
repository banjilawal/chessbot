# src/schema/terminus/quadrant/schema.py

"""
Module: schema.terminus.quadrant.schema
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from enum import Enum

import setting
from model import Vector


class QuadrantTerminus(Enum):
    """
    Role:
        -   Configuration Table
        -   Metadata Set


    Responsibilities:
        1.  Terminus of each quadrant

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
    
    NORTHWEST = (
        "northwest",
        Vector(x=0, y=0, )
    )
    NORTHEAST = (
        "northeast",
        Vector(x=setting.board.dimension.config.number_of_columns - 1, y=0)
    )
    SOUTHEAST = (
        "southeast",
        Vector(
            x=setting.board.dimension.config.number_of_columns - 1,
            y=setting.board.dimension.config.number_of_rows - 1,
        )
    )
    SOUTHWEST = (
        "southwest",
        Vector(
            x=0,
            y=setting.board.dimension.config.number_of_rows - 1,
        )
    )
    
    @property
    def orientation(self) -> str:
        return self._orientation
    
    @property
    def vector(self) -> Vector:
        return self._vector


