# src/ray/bounds/quadrant/ray.py

"""
Module: ray.bounds.quadrant.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Coord, Vector
from ray import RayBounds
from space import QuadrantTerminusHash


class QuadrantBounds(RayBounds):
    
    endpoint: QuadrantTerminusHash = QuadrantTerminusHash()
    
    def __init__(self, origin: Vector, terminus: Vector,):
        super().__init__(origin=origin, terminus=terminus)
        

    
    @classmethod
    def northeast_bounds(cls, coord: Coord,) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.endpoint.northeast,
        )
    
    @classmethod
    def northwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.endpoint.northwest
        )
    
    @classmethod
    def southeast_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.endpoint.southeast
        )
    
    @classmethod
    def southwest_bounds(cls, coord: Coord) -> QuadrantBounds:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            terminus=cls.endpoint.southwest
        )