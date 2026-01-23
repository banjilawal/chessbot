# src/chess/rank/model/concrete/pawn/vector/abstract.py

"""
Module: chess.rank.model.concrete.pawn.vector.abstract
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from abc import ABC
from typing import List

from chess.vector import Vector


class PawnVectorSet(ABC):
    _attack_targeting_vectors: List[Vector]
    _peaceful_destination_vectors: List[Vector]
    
    def __init__(
            self,
            attack_targeting_vectors: List[Vector],
            peaceful_destination_vectors: List[Vector]
    ):
        self._attack_targeting_vectors = attack_targeting_vectors
        self._peaceful_destination_vectors = peaceful_destination_vectors
        
        
    @property
    def attack_targeting_vectors(self) -> List[Vector]:
        return self._attack_targeting_vectors
    
    @property
    def peaceful_destination_vectors(self) -> List[Vector]:
        return self._peaceful_destination_vectors