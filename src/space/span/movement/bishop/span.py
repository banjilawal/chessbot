# src/space/span/movement/bishop/span.py

"""
Module: space.span.movement.bishop.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Bishop, Vector
from space import MovementVectorSet


class BishopMovementVectorSet(MovementVectorSet[Bishop]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a BishopBasis. Necessary for computing a BishopToken's destination vectors.

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
    
