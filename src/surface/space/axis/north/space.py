# src/space/axis/north/space.py

"""
Module: space.axis.north.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Vector
from surface import Axis


class NorthAxis(Axis):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Axis bounded between U(x_i, y_i) <= V(x_i, 0).

    Attributes:
        origin: Vector
        
    Provides:

    Super Class:
        Axis
    """
    
    def __init__(self, origin: Vector,):
        """
        Args:
            origin: Vector
        """
        super().__init__(
            origin=origin,
            destination=Vector(x=origin.x, y=0)
        )
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, NorthAxis):
            return self.origin == other.origin and self.destination == other.destination
        return False

        
    