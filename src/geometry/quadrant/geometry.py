# src/geometry/quadrant/geometry.py

"""
Module: geometry.quadrant.geometry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from geometry import Geometry


class Quadrant(Geometry):
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
        terminal_vector: Vector

    Provides:

    Super Class:
        Geometry
    """
    _terminal_vector: Vector
    
    def __init__(self, x_step: int, slope: int, terminal_vector: Vector):
        """
        Args:
            x_step: int
            slope: int
            terminal_vector: Vector
        """
        super().__init__(a=x_step, b=slope)
        self._terminal_vector = terminal_vector
        
    @property
    def x_step(self) -> int:
        return cast(int, self.a)
    
    @property
    def slope(self) -> int:
        return cast(int, self.b)
    
    @property
    def terminal_vector(self) -> Vector:
        return self._terminal_vector
        
    