# src/bounds/axis/bounds.py

"""
Module: bounds.axis.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


import setting
from bounds import RayBounds
from geometry import Axis

from model import Coord, Vector


class AxisBounds(RayBounds):

    
    def __init__(self, origin: Vector, terminus: Vector):
        super().__init__(origin=origin, terminus=terminus)
    
    
    @classmethod
    def east_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus = Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=coord.row,
            )
        )
    
    @classmethod
    def north_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=Vector(x=coord.column, y=coord.row),
        )
    
    @classmethod
    def south_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=Vector(
                x=coord.column,
                y=setting.board.dimension.config.number_of_rows - 1,
            )
        )
    
    @classmethod
    def west_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=Vector(x=coord.column, y=0)
        )