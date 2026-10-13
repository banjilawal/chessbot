# src/space/quadrant/northwest/space.py

"""
Module: space.quadrant.northwest.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.model import Vector
from domain.schema import QuadrantDestination
from surface.space.quadrant.northwest.space import Quadrant


class NorthwestQuadrant(Quadrant):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Quadrant bounded between U(x_i, y_i) <= V(0, 0).

    Attributes:
        origin: Vector
        destination: Vector = QuadrantDestination.NORTHWEST.vector
        
    Provides:

    Super Class:
        QuadrantSpace
    """
    
    def __init__(
            self,
            origin: Vector,
            destination: Vector = QuadrantDestination.NORTHWEST.vector,
    ):
        """
        Args:
            origin: Vector
            destination: Vector = QuadrantDestination.NORTHWEST.vector
        """
        super().__init__(origin=origin, destination=destination)
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    