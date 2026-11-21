# src/space/quadrant/northeast/space.py

"""
Module: space.quadrant.northeast.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantDestination, Vector
from surface import Quadrant


class NortheastQuadrant(Quadrant):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Quadrant bounded between U(x_i, y_i) <= V(num_columns - 1 , 0).

    Attributes:
        origin: Vector
        destination: Vector = QuadrantDestination.NORTHEAST.vector
        
    Provides:

    Super Class:
        QuadrantSpace
    """
    
    def __init__(
            self,
            origin: Vector,
            destination: Vector = QuadrantDestination.NORTHEAST.vector,
    ):
        """
        Args:
            origin: Vector
            destination: Vector = QuadrantDestination.NORTHEAST.vector
        """
        super().__init__(origin=origin, destination=destination)
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, NortheastQuadrant):
            return self.origin == other.origin and self.destination == other.destination
        return False
        
    