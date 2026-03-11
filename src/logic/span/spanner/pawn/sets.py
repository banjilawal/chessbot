# src/logic/span/spanner/pawn/vectors.py

"""
Module: logic.span.spanner.pawn.vectors
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from typing import Dict, List
from logic.vector import Vector

class PawnVectorSets:
    _opening_set: Dict[str, List[Vector]] = {
        "visit": [Vector(x=0, y=1), Vector(x=0, y=2), ],
        "attack": [
            Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1),
            Vector(x=0, y=2), Vector(x=-1, y=2), Vector(x=1, y=2),
        ],
    }
    _developed_set: Dict[str, List[Vector]] = {
        "visit": [Vector(x=0, y=1)],
        "attack": [Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1), ]
    }
    
    @property
    def opening_vector_sets(self) -> Dict[str, List[Vector]]:
        return self._opening_set
    
    @property
    def developed_vector_sets(self) -> Dict[str, List[Vector]]:
        return self._developed_set
    
    
    @property
    def to_list(self) -> List[Dict[str, List[Vector]]]:
        return [self._opening_set, self._developed_set]
        
        
    @property
    def to_dict(self) -> Dict[str, {}]:
        return {
            "opening_set": self._opening_set,
            "developed_set": self._developed_set,
        }