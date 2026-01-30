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
    """
    # ROLE: Configuration Information.

    # RESPONSIBILITIES:
    1.  Provides a read-ony sets of vectors for computing attack targets and peaceful destinations
        for a pawn that has not moved from its starting item.

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
            peaceful_destination_vectors=[Vector(x=0, y=1), Vector(x=0, y=2), ],
            attack_targeting_vectors=[Vector(x=0, y=2), Vector(x=-1, y=2), Vector(x=1, y=2),],
        )