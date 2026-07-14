# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations



from model import Vector
from ray import QuadrantRayBounds
from space import Space


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
        Line
    """
    _x_step: int
    _slope: int
    _bounds: QuadrantRayBounds
    _terminus: Vector
    
    def __init__(self, x_step: int, slope: int, bounds: QuadrantRayBounds):
        """
        Args:
            x_step: int
            slope: int
            bounds: QuadrantBounds
        """
        super().__init__()
        self._x_step = x_step
        self._slope = slope
        self._bounds = bounds
        
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def origin(self) -> Vector:
        return self._bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self._bounds.terminus

        
    