# src/register/axis/register.py

"""
Module: register.axis.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from model import Coord, Vector
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
    EAST_DELTA: Vector = Vector(x=1, y=0)
    NORTH_DELTA = Vector(x=0, y=-1)
    SOUTH_DELTA = Vector(x=0, y=1)
    WEST_DELTA = Vector(x=-1, y=0)
    
    _origin: Vector
    _delta: Vector
    
    
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
    
    @classmethod
    def east_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta=cls.EAST_DELTA,
        )
    
    @classmethod
    def north_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta=cls.NORTH_DELTA,
        )
    
    @classmethod
    def south_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta=cls.SOUTH_DELTA,
        )
    
    @classmethod
    def west_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta=cls.WEST_DELTA,
        )
    