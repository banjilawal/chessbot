# src/chess/rank/model/concrete/pawn/vector/opening.py

"""
Module: chess.rank.model.concrete.pawn.vector.opening
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.rank import PawnVectorSet
from chess.vector import Vector


class OpeningPawnVectorSet(PawnVectorSet):
    PEACEFUL_DESTINATION_VECTORS = [Vector(x=0, y=1), Vector(x=0, y=2), ],
    ATTACK_TARGETING_VECTORS = [Vector(x=0, y=2), Vector(x=-1, y=2), Vector(x=1, y=2), ]
    def __init__(
            self,
            attack_targeting_vectors: List[Vector] = ATTACK_TARGETING_VECTORS,
            peaceful_destination_vectors: List[Vector] = PEACEFUL_DESTINATION_VECTORS
    ):
        super().__init__(
            attack_targeting_vectors=attack_targeting_vectors,
            peaceful_destination_vectors=peaceful_destination_vectors
        )