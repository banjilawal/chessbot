# src/space/terminus/quadrant/space.py

"""
Module: space.terminus.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

import setting
from model import Vector


class QuadrantTerminusEntry:
    """
    Role:
        -   Lookup Table

    Responsibilities:
        1.  Provides an easy way of getting a quadrant's terminus.

    Attributes:
        northeast: Vector
        northwest: Vector
        southwest: Vector
        southeast: Vector
        
    Provides:

    Super Class:
    """
    
    _entry: Dict[str, Vector]

    def __init__(self):
        
        self._entry = {
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
        return self._entry["northwest"]
    
    @property
    def northeast(self) -> Vector:
        return self._entry["northeast"]
    
    @property
    def southwest(self) -> Vector:
        return self._entry["southwest"]
    
    @property
    def southeast(self) -> Vector:
        return self._entry["southeast"]