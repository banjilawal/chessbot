# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from space import QuadrantBounds, Space


class Quadrant(Space):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of a quadrant relative to a
            token's position.

    Attributes:
        x_step: int
        slope: int
        bounds: QuadrantBounds

    Provides:

    Super Class:
        Space
    """
    _x_step: int
    _slope: int
    _bounds: QuadrantBounds
    
    def __init__(self, x_step: int, slope: int, bounds: QuadrantBounds):
        """
        Args:
            x_step: int
            slope: int
            bounds: QuadrantBounds
        """
        super().__init__(bounds=bounds)
        self._x_step = x_step
        self._slope = slope
        
    @property
    def bounds(self) -> QuadrantBounds:
        return cast(QuadrantBounds, self.bounds)
        
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def origin(self) -> Vector:
        return self.bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self.bounds.terminus
    
    
    @classmethod
    def northeast(cls, origin: Vector) -> Quadrant:
        return cls(
            bounds=QuadrantBounds.northeast(origin=origin)
        )

        
    