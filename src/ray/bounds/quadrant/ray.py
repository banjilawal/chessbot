# src/ray/bounds/quadrant/ray.py

"""
Module: ray.bounds.quadrant.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from ray import RayBounds
from space import QuadrantTerminusEntry


class QuadrantRayBounds(RayBounds):
    
    terminus_entry: QuadrantTerminusEntry = QuadrantTerminusEntry()
    
    def __init__(self, origin: Vector, terminus: Vector,):
        super().__init__(origin=origin, terminus=terminus)
        

    
    @classmethod
    def northeast_bounds(cls, origin: Vector) -> QuadrantRayBounds:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.northeast,
        )
    
    @classmethod
    def northwest_bounds(cls, origin: Vector) -> QuadrantRayBounds:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.northwest
        )
    
    @classmethod
    def southeast_bounds(cls, origin: Vector) -> QuadrantRayBounds:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.southeast
        )
    
    @classmethod
    def southwest_bounds(cls, origin: Vector) -> QuadrantRayBounds:
        return cls(
            origin=origin,
            terminus=cls.terminus_entry.southwest
        )