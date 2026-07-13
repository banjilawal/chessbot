# src/register/axis/east/register.py

"""
Module: register.axis.east.register_
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from register import Axis


class EastAxis(Axis):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of a axis relative to a
            token's position.

    Attributes:
        origin: Vector
        delta: Vector

    Provides:

    Super Class:
        Register
    """
    DELTA = Vector(x=1, y=0)
    
    def __init__(self, origin: Vector,):
        """
        Args:
            origin: Vector
        """
        super().__init__(origin=origin, delta=self.DELTA,)

        
    