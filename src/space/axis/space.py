# src/space/axis/space.py

"""
Module: space.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Coord, Vector
from space import AxisBounds, AxisDeltaEntry, DeltaBound, DeltaBoundHash, Space


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
    delta_entry: AxisDeltaEntry = AxisDeltaEntry()
    hash: DeltaBoundHash = DeltaBoundHash(Coord(0,0))
    
    _origin: Vector
    _delta: Vector
    _delta_bound: DeltaBound
    _bounds: AxisBounds
    
    def __init__(self, delta: Vector, bounds: AxisBounds):
        """
        Args:
            delta: Vector
            bounds: AxisBounds
        """
        super().__init__()
        self._delta = delta
        self._bounds = bounds
        
    @property
    def origin(self) -> Vector:
        return self._bounds.origin
    
    @property
    def terminus(self) -> Vector:
        return self._bounds.terminus
    
    @property
    def delta_bound(self) -> DeltaBound:
        return self._delta_bound
    
    @classmethod
    def east_axis(cls, origin: Vector) -> Axis:
        return cls(
            delta=cls.delta_entry.east,
            bounds=AxisBounds.east(origin=origin),
        )
    
    @classmethod
    def north_axis(cls, origin: Vector) -> Axis:
        return cls(
            delta=cls.delta_entry.north,
            bounds=AxisBounds.north(origin=origin)
        )
    
    @classmethod
    def south_axis(cls, origin: Vector) -> Axis:
        return cls(
            delta=cls.delta_entry.south,
            bounds=AxisBounds.south(origin=origin)
        )
    
    @classmethod
    def west_axis(cls, origin: Vector) -> Axis:
        return cls(
            delta=cls.delta_entry.west,
            bounds=AxisBounds.west(origin=origin)
        )
    