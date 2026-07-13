# src/bounds/south/bounds.py

"""
Module: bounds.axis.south.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

import setting.board.dimension.config
from bounds import AxisBounds
from model import Coord, Vector
from register import SouthAxis


class SouthAxisBounds(AxisBounds):
    _origin: SouthAxis
    _terminus: Vector
    
    
    def __init__(self, coord: Coord):
        self._origin = SouthAxis(Vector(x=coord.column, y=coord.row))
        self._terminus = Vector(
            x=coord.column,
            y=setting.board.dimension.config.number_of_rows - 1
        )

    @property
    def origin(self) -> SouthAxis:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    def compute(self) -> List[Vector]:
        cursor = self._axis.origin
        vectors: List[Vector] = []
        
        while cursor != self._terminus:
            vectors.append(cursor)
            cursor = Vector(
                x=self._axis.delta.x + cursor.x,
                y=self._axis.delta.y + cursor.y
            )
        return vectors