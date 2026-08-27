# src/space/quadrant/southeast/space.py

"""
Module: space.quadrant.southeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.model import Vector
from space.quadrant.southeast.space import Quadrant


class SoutheastQuadrant(Quadrant):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Quadrant bounded between U(x_i, y_i) <= V(num_columns - 1, num_rows - 1).

    Attributes:

    Provides:

    Super Class:
        QuadrantSpace
    """
    
    def __init__(self, origin: Vector, terminus: Vector):
        """
        Args:
            origin: Vector
            terminus: Vector
        """
        super().__init__(origin=origin, terminus=terminus)
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    