# src/bounds/east/bounds.py

"""
Module: bounds.axis.east.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


import setting.board.dimension.config
from bounds import AxisBounds
from model import Coord, Vector


from register import EastAxis


class EastAxisBounds(AxisBounds):
    _origin: EastAxis
    _terminus: Vector
    
    
    def __init__(self, coord: Coord):
        self._origin = EastAxis(origin=Vector(x=coord.column, y=coord.row))
        self._terminus = Vector(
            x=setting.board.dimension.config.number_of_columns - 1,
            y=coord.row
        )
        
    @property
    def origin(self) -> EastAxis:
        return self._origin

    @property
    def terminus(self) -> Vector:
        return self._terminus
