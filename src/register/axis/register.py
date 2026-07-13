# src/register/axis/register.py

"""
Module: register.axis.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Vector
from register import Register


class Axis(Register):
    """
    Role:
        -   Addressing
        -   Data-Holder

    Responsibilities:
        1.  Defines the delta_x/delta_y and bounds of an axis relative to a
            token's position.

    Attributes:
        origin: Vector
        delta: Vector

    Provides:

    Super Class:
        Register
    """
    
    def __init__(self, origin: Vector, delta: Vector):
        """
        Args:
            delta: Vector
            origin: Vector
        """
        super().__init__(a=origin, b=delta)
        
    @property
    def origin(self) -> Vector:
        return cast(Vector, self.a)
    
    @property
    def delta(self) -> Vector:
        return cast(Vector, self.b)
    