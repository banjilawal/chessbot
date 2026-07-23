# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Vector
from space import Space


class QuadrantSpace(Space):
    """
    Role:
        -   Definition

    Responsibilities:
        1.  A diagonal line whose root is the Space's origin.
        2.  A quadrant is bounded by two axis.

    Attributes:
        origin: Vector
        terminus: Vector
        
    Provides:

    Super Class:
        Space
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
        

        
    