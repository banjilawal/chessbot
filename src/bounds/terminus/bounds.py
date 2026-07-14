# src/bounds/terminus/bounds.py

"""
Module: bounds.terminus.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

import setting
from model import Vector


class QuadrantTerminus:
    
    NORTHWEST_TERMINUS: Vector = Vector(x=0, y=0, )
    NORTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=0,
    )
    SOUTHEAST_TERMINUS = Vector(
        x=setting.board.dimension.config.number_of_columns - 1,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    SOUTHWEST_TERMINUS = Vector(
        x=0,
        y=setting.board.dimension.config.number_of_rows - 1,
    )
    
    _hash: Dict[str, Vector]
    
    def __init__(self):
        
        self._hash = {
            "northwest": self.NORTHWEST_TERMINUS,
            "northeast": self.NORTHEAST_TERMINUS,
            "southeast": self.SOUTHEAST_TERMINUS,
            "southwest": self.SOUTHWEST_TERMINUS,
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