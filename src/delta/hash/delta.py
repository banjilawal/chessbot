# src/delta/hash/delta.py

"""
Module: delta.hash.delta
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from bounds import AxisBounds
from geometry import AxisDelta, DeltaBound
from model import Coord


class DeltaBoundHash:
    _axis_delta: AxisDelta = AxisDelta()
    
    _hash: Dict[str: DeltaBound]
    
    def __init__(self, coord: Coord):
        self._axis_delta = AxisDelta()
        
        self._hash = {
            "north": DeltaBound(
                delta=self._axis_delta.north,
                bounds=AxisBounds.north_bounds(coord=coord)
            ),
            "east": DeltaBound(
                delta=self._axis_delta.east,
                bounds=AxisBounds.east_bounds(coord=coord)
            ),
            "south": DeltaBound(
                delta=self._axis_delta.south,
                bounds=AxisBounds.south_bounds(coord=coord),
            ),
            "west": DeltaBound(
                delta=self._axis_delta.west,
                bounds=AxisBounds.west_bounds(coord=coord),
            ),
        }
        
    @property
    def north(self) -> DeltaBound:
        return self._hash["north"]
    
    @property
    def east(self) -> DeltaBound:
        return self._hash["east"]
    
    @property
    def south(self) -> DeltaBound:
        return self._hash["south"]
    
    @property
    def west(self) -> DeltaBound:
        return self._hash["west"]