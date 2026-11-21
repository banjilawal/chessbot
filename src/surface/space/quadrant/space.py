# src/space/quadrant/space.py

"""
Module: space.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.model import Vector
from surface.space.quadrant.space import Space


class Quadrant(Space):
    """
    Role:
        -   Definition

    Responsibilities:
        1.  A diagonal line whose root is the Space's origin.
        2.  A quadrant is bounded by two axis.

    Attributes:
        origin: Vector
        destination: Vector
        
    Provides:

    Super Class:
        Space
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
        if isinstance(other, Quadrant):
            return self.origin == other.origin and self.destination == other.destination
        return False
        

        
    