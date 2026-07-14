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


class QuadrantTerminusHash:
    
    _hash: Dict[str, Vector]
    
    def __init__(self):
        
        self._hash = {
            "northwest": Vector(x=0, y=0,),
            "northeast": Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=0,
            ),
            "southeast": Vector(
                x=setting.board.dimension.config.number_of_columns - 1,
                y=setting.board.dimension.config.number_of_rows - 1,
            ),
            "southwest": Vector(
                x=0,
                y=setting.board.dimension.config.number_of_rows - 1,
            ),
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