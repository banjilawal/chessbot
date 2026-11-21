# src/space/axis/east/space.py

"""
Module: space.axis.east.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDestination, Vector
from surface import Axis


class EastAxis(Axis):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Axis bounded between U(x_i, y_i) <= V(num_columns - 1, y_i).

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
            destination=Vector(
                x=AxisDestination.EAST.vector.x,
                y=origin.y
            )
        )
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, EastAxis):
            return self.origin == other.origin and self.destination == other.destination
        return False
        
    