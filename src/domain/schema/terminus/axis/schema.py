# src/domain/schema/terminus/axis/schema.py

"""
Module: domain.schema.terminus.axis.schema
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from enum import Enum

from domain.model import Vector


class AxisTerminus(Enum):
    """
    Role:
        -  Configuration Table
        -  Metadata Set


    Responsibilities:
        1.  Terminus of each axis

    Attributes:
        orientation: str
        terminus: Vector

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
    
    NORTH = (
        "north",
        Vector(
            x=0,
            y=-config.setting.board.dimension.config.number_of_rows - 1,
        )
    )
    EAST = (
        "east",
        Vector(
            x=config.setting.board.dimension.config.number_of_columns - 1,
            y=0,
        )
    )
    SOUTH = (
        "south",
        Vector(
            x=0,
            y=config.setting.board.dimension.config.number_of_rows - 1,
        )
    )
    WEST = (
        "west",
        Vector(
            x=config.setting.board.dimension.config.number_of_columns - 1,
            y=0,
        )
    )
    
    @property
    def orientation(self) -> str:
        return self._orientation
    
    @property
    def vector(self) -> Vector:
        return self._vector