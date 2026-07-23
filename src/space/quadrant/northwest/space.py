# src/space/quadrant/northwest/space.py

"""
Module: space.quadrant.northwest.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from schema import QuadrantTerminus
from space import QuadrantSpace


class NorthwestQuadrant(QuadrantSpace):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Quadrant bounded between U(x_i, y_i) <= V(0, 0).

    Attributes:
        origin: Vector
        terminus: Vector = QuadrantTerminus.NORTHWEST.vector
        
    Provides:

    Super Class:
        QuadrantSpace
    """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Vector = QuadrantTerminus.NORTHWEST.vector,
    ):
        """
        Args:
            origin: Vector
            terminus: Vector = QuadrantTerminus.NORTHWEST.vector
        """
        super().__init__(origin=origin, terminus=terminus)
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    