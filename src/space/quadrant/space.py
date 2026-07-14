# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from space.quadrant.space import Space
from model import Vector



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
        terminus: Vector

    Provides:

    Super Class:
        Line
    """
    _x_step: int
    _slope: int
    _terminus: Vector
    
    def __init__(self, x_step: int, slope: int, terminus: Vector):
        """
        Args:
            x_step: int
            slope: int
            terminus: Vector
        """
        super().__init__()
        self._x_step = x_step
        self._slope = slope
        self._terminus = terminus
        
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def terminus(self) -> Vector:
        return self._terminus

        
    