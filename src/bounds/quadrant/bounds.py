# src/bounds/quadrant/bounds.py

"""
Module: bounds.quadrant.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

import setting
from geometry.quadrant import Quadrant
from model import Coord, Vector


class QuadrantBounds:
    NORTHWEST_TERMINUS = Vector(x=0, y=0, )
    NORTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=0,
    )
    SOUTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    SOUTHWEST_TERMINUS = Vector(
        x=0,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    _origin: Vector
    _terminus: Vector
    
    def __init__(self, origin: Vector, terminus: Vector,):
        self._origin = origin
        self._quadrant = terminus
    
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @classmethod
    def northeast_bounds(
            cls,
            coord: Coord,
    ) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.NORTHEAST_TERMINUS,
        )
    
    @classmethod
    def northwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.NORTHWEST_TERMINUS
        )
    
    @classmethod
    def southeast_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.NORTHEAST_TERMINUS
        )
    
    @classmethod
    def southwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.SOUTHWEST_TERMINUS
        )