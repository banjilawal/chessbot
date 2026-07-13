# src/bounds/bounds.py

"""
Module: bounds.axis.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

import setting
from model import Coord, Vector
from register import Axis, EastAxis


class AxisBounds(ABC):
    _axis: Axis
    _terminus: Vector
    
    def __init__(self, axis: Axis, terminus):
        self._axis = axis
        self._terminus = terminus
    
    
    @property
    def axis(self) -> Axis:
        return self._axis
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @classmethod
    def east_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            axis=Axis.east_axis(coord),
            terminus = Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=coord.row,
            )
        )
    
    @classmethod
    def north_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            axis=Axis.north_axis(coord),
            terminus=Vector(x=coord.column, y=coord.row),
        )
    
    @classmethod
    def south_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            axis=Axis.south_axis(coord),
            terminus=Vector(
                x=coord.column,
                y=setting.board.dimension.config.number_of_rows - 1,
            )
        )
    
    @classmethod
    def west_bounds(cls, coord: Coord) -> AxisBounds:
        return cls(
            axis=Axis.west_axis(coord),
            terminus=Vector(x=coord.column, y=0)
        )