# src/space/bounds/axis/space.py

"""
Module: space.bounds.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


import setting


from model import Vector
from space import SpaceBounds


class AxisBounds(SpaceBounds):

    
    def __init__(self, origin: Vector, terminus: Vector):
        super().__init__(origin=origin, terminus=terminus)
    
    
    @classmethod
    def east(cls, origin: Vector) -> AxisBounds:
        return cls(
            origin=origin,
            terminus = Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=origin.y,
            )
        )
    
    @classmethod
    def north(cls, origin: Vector) -> AxisBounds:
        return cls(
            origin=origin,
            terminus=Vector(x=origin.x, y=0),
        )
    
    @classmethod
    def south(cls, origin: Vector) -> AxisBounds:
        return cls(
            origin=origin,
            terminus=Vector(
                x=origin.x,
                y=setting.board.dimension.config.number_of_rows - 1,
            )
        )
    
    @classmethod
    def west(cls, origin: Vector) -> AxisBounds:
        return cls(
            origin=Vector(x=0, y=origin.y),
            terminus=origin
        )