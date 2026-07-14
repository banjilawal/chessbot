# src/geometry/quadrant/geometry.py

"""
Module: geometry.quadrant.geometry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from blueprint import NortheastQuadrantBlueprint
from model import Vector
from register import Register


class Quadrant(Register):
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
        Geometry
    """
    _terminus: Vector
    
    def __init__(self, x_step: int, slope: int, terminus: Vector):
        """
        Args:
            x_step: int
            slope: int
            terminus: Vector
        """
        super().__init__(a=x_step, b=slope)
        self._terminus = terminus
        
    @property
    def x_step(self) -> int:
        return cast(int, self.a)
    
    @property
    def slope(self) -> int:
        return cast(int, self.b)
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @classmethod
    def northeast_quadrant(
            cls,
            blueprint: NortheastQuadrantBlueprint = NortheastQuadrantBlueprint()
    ):
        
    