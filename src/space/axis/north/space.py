# src/space/axis/north/space.py

"""
Module: space.axis.north.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain.model import Vector
from space.axis.north.space import Axis


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
            terminus=Vector(x=origin.x, y=0)
        )
    
    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if not isinstance(other, type(self)):
            return False
        return True

        
    