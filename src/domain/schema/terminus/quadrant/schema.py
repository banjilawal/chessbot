# src/domain/schema/terminus/quadrant/schema.py

"""
Module: domain.schema.terminus.quadrant.schema
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum

from domain.model import Vector


class QuadrantTerminus(Enum):
    """
    Role:
        - Configuration Table
        -  Metadata Set


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
        Vector(x=config.setting.board.dimension.config.number_of_columns - 1, y=0)
    )
    SOUTHEAST = (
        "southeast",
        Vector(
            x=config.setting.board.dimension.config.number_of_columns - 1,
            y=config.setting.board.dimension.config.number_of_rows - 1,
        )
    )
    SOUTHWEST = (
        "southwest",
        Vector(
            x=0,
            y=config.setting.board.dimension.config.number_of_rows - 1,
        )
    )
    
    @property
    def orientation(self) -> str:
        return self._orientation
    
    @property
    def vector(self) -> Vector:
        return self._vector


