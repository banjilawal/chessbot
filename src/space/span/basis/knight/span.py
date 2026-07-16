# src/space/span/basis/knight/space/span.py

"""
Module: space.span.basis.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Knight, Vector
from space.span import KnightMovementVectorSet, VectorBasis


class KnightVectorBasis(VectorBasis[Knight]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors by adding a Knight's current position to each of the
            Knight's movement_vectors

    Attributes:
            origin: Vector
            movement_vectors: Optional[KnightMovementVectorSet]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[KnightMovementVectorSet] | None = KnightMovementVectorSet(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[KnightMovementVectorSet]
        """
        super().__init__(origin=origin, movement_vectors=movement_vectors)
