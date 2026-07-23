# src/space/pawn/space.py

"""
Module: space.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from model import Vector
from space.basis import PawnAttackOffsetPattern


class DevelopedAttackOffsetPattern(PawnAttackOffsetPattern):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a DevelopedPawnAttackBasis. Necessary for computing a PawnToken's
            attack destination vectors, after its first move.

    Attributes:
        offsets: DeltaSet

    Provides:

    Super Class:
        PawnAttackOffsetPattern
    """
    
    def __init__(self,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(
            maneuver_vectors=VectorSet(
                (Vector(x=-1, y=1), Vector(x=1, y=1),)
            )
        )
    
    
