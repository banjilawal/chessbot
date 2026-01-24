# src/chess/rank/model/concrete/pawn/vector/developed.py

"""
Module: chess.rank.model.concrete.pawn.vector.developed
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from typing import List

from chess.vector import Vector
from chess.rank import PawnVectorSet

class DevelopedPawnVectorSet(PawnVectorSet):
    """
    # ROLE: Configuration Information.

    # RESPONSIBILITIES:
    1.  Provides a read-ony sets of vectors for computing attack targets and peaceful destinations
        for a pawn that has made its first move.

    # PARENT:
        *   PawnVectorSet

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See PawnVectorSet super class for inherited attributes.
    """
    def __init__(self,):
        super().__init__(
            peaceful_destination_vectors=[Vector(x=0, y=1)],
            attack_targeting_vectors=[Vector(x=0, y=1), Vector(x=-1, y=1), Vector(x=1, y=1)],
        )