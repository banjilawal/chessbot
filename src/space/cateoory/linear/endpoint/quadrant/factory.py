# src/space/linear/segment/quadrant/linear.py

"""
Module: space.linear.segment.quadrant.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from register import VectorRegister
from space.cateoory.linear.category.quadrant.table import QuadrantTerminus


class QuadrantEndpointFactory:
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Prevent ArrayIndexOutOfSegment errors by calculating the upper and lower segment
            vectors of a Quadrant's incline.

    Attributes:
        terminus_entry: QuadrantTerminusEntry
        
    Provides:
        -   def northeast(cls, origin: Vector) -> QuadrantSegment
        -   def northwest(cls, origin: Vector) -> QuadrantSegment
        -   def southwest(cls, origin: Vector) -> QuadrantSegment
        -   def southeast(cls, origin: Vector) -> QuadrantSegment

    Super Class:
        SpaceSegment

    WARNING:
        *****===ONLY_INSTANTIATE_WITH_THE_FACTORY_METHODS===*****
    """
    _origin: Vector
    
    def __init__(self, origin: Vector):
        """
        Args:
            origin: Vector
        """
        self._origin = origin
        
    @property
    def origin(self) -> Vector:
        return self._origin
        

    def northeast_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.NORTHEAST.terminus,
        )
    
    def northwest_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.NORTHWEST.terminus
        )
    
    def southeast_endpoints(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.SOUTHEAST.terminus
        )
    
    def southwest(self) -> VectorRegister:
        return VectorRegister(
            u=self._origin,
            v=QuadrantTerminus.SOUTHWEST.terminus
        )