# src/delta/py

"""
Module: delta.geometry
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from model import Vector


class AxisDelta:
    _EAST_DELTA: Vector = Vector(x=1, y=0)
    _NORTH_DELTA: Vector = Vector(x=0, y=-1)
    _SOUTH_DELTA: Vector = Vector(x=0, y=1)
    _WEST_DELTA: Vector = Vector(x=-1, y=0)
    
    _hash: Dict[str, Vector]
    
    def __init__(self):
        self._hash = {
            "east": self._EAST_DELTA,
            "north": self._NORTH_DELTA,
            "south": self._SOUTH_DELTA,
            "west": self._WEST_DELTA,
        }
        
    @property
    def east(self) -> Vector:
        return self._hash["east"]
    
    @property
    def north(self) -> Vector:
        return self._hash["north"]
    
    @property
    def west(self) -> Vector:
        return self._hash["west"]
    
    @property
    def south(self) -> Vector:
        return self._hash["south"]