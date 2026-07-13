# src/bounds/west/bounds.py

"""
Module: bounds.axis.west.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from bounds import AxisBounds
from model import Coord, Vector
from register import WestAxis


class WestAxisBounds(AxisBounds):
    _origin: WestAxis
    _terminus: Vector
    
    def __init__(self, coord: Coord):
        self._origin = WestAxis(Vector(x=coord.column, y=coord.row))
        self._terminus = Vector(x=coord.column, y=0)
        self._axis = WestAxis(origin=self._origin)

    @property
    def origin(self) -> WestAxis:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    
    
