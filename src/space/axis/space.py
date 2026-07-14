# src/space/axis/space.py

"""
Module: space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Coord, Vector
from space import DeltaBound, DeltaBoundHash, Space


class Axis(Space):
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
        Space
    """
    hash: DeltaBoundHash = DeltaBoundHash()
    
    _origin: Vector
    _delta_bound: DeltaBound
    
    def __init__(self, origin: Vector, delta_bound: DeltaBound):
        """
        Args:
            origin: Vector
            delta_bound: DeltaBound
        """
        super().__init__()
        self._origin = origin
        self._delta_bound = delta_bound
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self.delta_bound.bounds.terminus
    
    @property
    def delta_bound(self) -> DeltaBound:
        return self._delta_bound
    
    @classmethod
    def east_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta_bound=cls.hash.east,
        )
    
    @classmethod
    def north_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta_bound=cls.hash.north,
        )
    
    @classmethod
    def south_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta_bound=cls.hash.south,
        )
    
    @classmethod
    def west_axis(cls, coord: Coord) -> Axis:
        return cls(
            origin=Vector(x=coord.column, y=coord.row),
            delta_bound=cls.hash.west
        )
    