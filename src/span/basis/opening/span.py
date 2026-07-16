# src/span/basis/pawn/span.py

"""
Module: span.basis.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Pawn, Vector
from span import VectorBasis


class PawnVectorBasis(VectorBasis[Pawn]):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfBasis errors by calculating the last point in the direction
            of travel

    Attributes:

    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: VectorSet | None = RankVectorSetTable().pawn_movement_vectors,
    ):
        super().__init__(origin=origin, movement_vectors=movement_vectors)
