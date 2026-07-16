# src/span/basis/knight/span.py

"""
Module: span.basis.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple

from model import Knight, Vector
from span import VectorBasis, VectorSet


class KnightVectorBasis(VectorBasis[Knight]):
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
            movement_vectors: VectorSet | None = RankVectorSetTable().knight_movement_vectors,
    ):
        super().__init__(origin=origin, movement_vectors=movement_vectors)
