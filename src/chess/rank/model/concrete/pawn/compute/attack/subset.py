# src/chess/rank/model/concrete/pawn/compute/attack/subset.py

"""
Module: chess.rank.model.concrete.pawn.compute.attack.subset
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from enum import Enum
from typing import List

from chess.vector import Vector


class AttackVectorSubset(Enum):
    def __new__(cls, vectors: List[Vector]):
        obj = object.__new__(cls)
        obj._vectors = vectors
        return obj
    
    OPENING = [Vector(x=0, y=2), Vector(x=-1, y=2), Vector(x=1, y=2),]
    DEVELOPED = [Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1),]
    
    @property
    def vectors(self) -> List[Vector]:
        return self._vectors

