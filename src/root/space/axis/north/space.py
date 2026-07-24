# src/space/axis/north/space.py

"""
Module: space.axis.north.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from space import AxialSpace


class NorthAxis(AxialSpace):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Axis bounded between U(x_i, y_i) <= V(x_i, 0).

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
            terminus=Vector(x=origin.x, y=0)
        )
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    