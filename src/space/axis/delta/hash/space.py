# src/space/axis/delta/hash/space/axis/space.axis.delta.py

"""
Module: space.axis.delta.hash.delta
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from space.bounds import AxisBounds
from space.axis.delta import AxisDeltaEntry, DeltaBound
from model import Coord


class DeltaBoundHash:
    _axis_delta: AxisDeltaEntry = AxisDeltaEntry()
    
    _hash: Dict[str: DeltaBound]
    
    def __init__(self, coord: Coord):
        self._axis_delta = AxisDeltaEntry()
        
        self._hash = {
            "north": DeltaBound(
                delta=self._axis_space.axis.delta.north,
                bounds=AxisBounds.north(coord=coord)
            ),
            "east": DeltaBound(
                delta=self._axis_space.axis.delta.east,
                bounds=AxisBounds.east(coord=coord)
            ),
            "south": DeltaBound(
                delta=self._axis_space.axis.delta.south,
                bounds=AxisBounds.south(coord=coord),
            ),
            "west": DeltaBound(
                delta=self._axis_space.axis.delta.west,
                bounds=AxisBounds.west(coord=coord),
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