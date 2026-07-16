# src/space/span/movement/pawn/space/span.py

"""
Module: space.span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from space.span import PawnMovementVectorSet


class PawnAttackVectorSet(ABC, PawnMovementVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a PawnBasis. They are necessary for computing a PawnToken's
            destination vectors.

    Attributes:
        movement_vectors: DeltaSet

    Provides:

    Super Class:
        MovementVectorSet
    """
    
    def __init__(self, movement_vectors: VectorSet):
        """
        Args:
            movement_vectors: MovementVectorSet
        """
        super().__init__(movement_vectors=movement_vectors)
    
    
