# src/space/span/movement/pawn/span.py

"""
Module: space.span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from model import Vector
from space.span import PawnAttackVectorSet


class DevelopedAttackVectorSet(PawnAttackVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a DevelopedPawnAttackBasis. Necessary for computing a PawnToken's
            attack destination vectors, after its first move.

    Attributes:
        movement_vectors: DeltaSet

    Provides:

    Super Class:
        PawnAttackVectorSet
    """
    
    def __init__(self,):
        """
        Args:
            movement_vectors: VectorSet
        """
        super().__init__(
            movement_vectors=VectorSet(
                (Vector(x=-1, y=1), Vector(x=1, y=1),)
            )
        )
    
    
