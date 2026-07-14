# src/space/quadrant/terminus/space.py

"""
Module: space.quadrant.terminus.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

import setting
from model import Vector


class QuadrantTerminus:
    
    _NORTHWEST_TERMINUS: Vector = Vector(x=0, y=0, )
    _NORTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=0,
    )
    _SOUTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    _SOUTHWEST_TERMINUS = Vector(
        x=0,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    
    _hash: Dict[str, Vector]
    
    def __init__(self):
        
        self._hash = {
            "northwest": self._NORTHWEST_TERMINUS,
            "northeast": self._NORTHEAST_TERMINUS,
            "southeast": self._SOUTHEAST_TERMINUS,
            "southwest": self._SOUTHWEST_TERMINUS,
        }
        
    @property
    def northwest(self) -> Vector:
        return self._hash["northwest"]
    
    @property
    def northeast(self) -> Vector:
        return self._hash["northeast"]
    
    @property
    def southwest(self) -> Vector:
        return self._hash["southwest"]
    
    @property
    def southeast(self) -> Vector:
        return self._hash["southeast"]