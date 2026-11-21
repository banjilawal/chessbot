# src/space/quadrant/southeast/space.py

"""
Module: space.quadrant.southeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Vector
from surface import Quadrant


class SoutheastQuadrant(Quadrant):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Quadrant bounded between U(x_i, y_i) <= V(num_columns - 1, num_rows - 1).

    Attributes:

    Provides:

    Super Class:
        Quadrant
    """
    
    def __init__(self, origin: Vector, destination: Vector):
        """
        Args:
            origin: Vector
            destination: Vector
        """
        super().__init__(origin=origin, destination=destination)
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, SoutheastQuadrant):
            return self.origin == other.origin and self.destination == other.destination
        return False

        
    