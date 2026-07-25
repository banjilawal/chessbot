# src/recurrence/table/quadrant/space.py

"""
Module: recurrence.table.quadrant.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from model import Vector
from space import (
    Quadrant, NortheastQuadrant, NorthwestQuadrant, SoutheastQuadrant, SpaceReservoir, SouthwestQuadrant
)

class QuadrantReservoir(SpaceReservoir[Quadrant]):
    _expected_size: int
    _hash_table: Dict[str, Quadrant]
    
    def __init__(self, origin: Vector,):
        super().__init__(origin=origin)
        
        self._hash_table = {
            "northeast_quadrant": NortheastQuadrant(self.origin),
            "northwest_quadrant": NorthwestQuadrant(self.origin),
            "southeast_quadrant": SoutheastQuadrant(self.origin),
            "southwest_quadrant": SouthwestQuadrant(self.origin),
        }
        self._expected_size = len(self._hash_table)
        
        
    @property
    def hash_table(self) -> Dict[str, Quadrant]:
        return self._hash_table

    @property
    def size(self) -> int:
        return len(self._hash_table)
    
    @property
    def expected_size(self) -> int:
        return self._expected_size
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_expected_size(self) -> bool:
        return self.size == self._expected_size
    
    @property
    def is_wrong_size(self) -> bool:
        return not self.is_expected_size
    
    @property
    def is_quadrant_hash_set(self) -> bool:
        for key in self._hash_table.keys():
            if not isinstance(self._hash_table[key], Quadrant):
                return False
        return True
    
    @property
    def is_not_quadrant_hash_set(self) -> bool:
        return not self.is_quadrant_hash_set
    

