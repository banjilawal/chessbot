# src/space/axis/south/space.py

"""
Module: space.axis.south.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDestination, Vector
from surface import Axis


class SouthAxis(Axis):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Axis bounded between U(x_i, y_i) <= V(x_i, num_rows - 1).

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
                x=0,
                y=AxisDestination.SOUTH.vector.y
            )
        )
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, SouthAxis):
            return self.origin == other.origin and self.destination == other.destination
        return False

        
    