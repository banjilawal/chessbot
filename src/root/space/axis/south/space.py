# src/space/axis/south/space.py

"""
Module: space.axis.south.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from schema import AxisTerminus
from space import AxialSpace


class SouthAxis(AxialSpace):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Axis bounded between U(x_i, y_i) <= V(x_i, num_rows - 1).

    Attributes:
        origin: Vector
        
    Provides:

    Super Class:
        AxisSpace
    """
    
    def __init__(self, origin: Vector,):
        """
        Args:
            origin: Vector
        """
        super().__init__(
            origin=origin,
            terminus=Vector(
                x=0,
                y=AxisTerminus.SOUTH.vector.y
            )
        )
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    