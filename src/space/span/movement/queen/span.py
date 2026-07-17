# src/space/span/movement/queen/space/span.py

"""
Module: space.span.movement.queen.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Queen, Vector
from space import MovementVectorSet


class QueenMovementVectorSet(MovementVectorSet[Queen]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a QueenBasis. Necessary for computing a QueenToken's destination vectors.

    Attributes:
        movement_vectors: VectorSet

    Provides:

    Super Class:
        MovementVectorSet
    """
    
    def __init__(self,):
        """
        Args:t
        """
        super().__init__(
            movement_vectors=VectorSet(
                    (
                        Vector(1, 0), Vector(-1, 0), Vector(0, 1),
                        Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)
                    )
            )
        )
    
