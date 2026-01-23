# src/chess/rank/model/concrete/pawn/compute/category.py

"""
Module: chess.rank.model.concrete.pawn.compute.category
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from enum import Enum
from typing import List

from chess.vector import Vector


class PawnVectorCategory(Enum):
    def __new__(cls, peaceful_vectors: List[Vector], attack_vectors: List[Vector]):
        obj = object.__new__(cls)
        obj._peaceful_vectors = peaceful_vectors
        obj._attack_vectors = attack_vectors
        return obj
    
    OPENING_MOVE = (
        [Vector(x=0, y=1), Vector(x=0, y=2),],
        [Vector(x=0, y=2), Vector(x=-1, y=2), Vector(x=1, y=2),]
    ),
    DEVELOPED_MOVE = (
        [Vector(x=0, y=1)],
        [Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1),]
    )
    
    @property
    def peaceful_vectors(self) -> List[Vector]:
        return self._peaceful_vectors
    
    @property
    def attack_vectors(self) -> List[Vector]:
        return self._attack_vectors

