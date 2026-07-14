# src/bounds/quadrant/bounds.py

"""
Module: bounds.quadrant.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from bounds import RayBounds
from bounds.terminus.bounds import QuadrantTerminus
from model import Coord, Vector


class QuadrantBounds(RayBounds):
    
    terminus: QuadrantTerminus = QuadrantTerminus()
    
    def __init__(self, origin: Vector, terminus: Vector,):
        super().__init__(origin=origin, terminus=terminus)

    
    @classmethod
    def northeast_bounds(cls, coord: Coord,) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.terminus.northeast,
        )
    
    @classmethod
    def northwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.terminus.northwest
        )
    
    @classmethod
    def southeast_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.terminus.southeast
        )
    
    @classmethod
    def southwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.terminus.southwest
        )