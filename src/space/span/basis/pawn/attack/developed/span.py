# src/space/span/basis/pawn/attack/developed/span.py

"""
Module: space.span.basis.pawn.attack.developed.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from space import DestinationSpanComputer, DevelopedAttackVectorSet, PawnAttackVectorBasis


class DevelopedPawnAttackVectorBasis(PawnAttackVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors for a Pawn which has not made its developed move.

    Attributes:
        origin: Vector
        movement_vectors: Optional[DevelopedAttackVectorSet]
        destination_span_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnAttackVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[DevelopedAttackVectorSet] |
                              None = DevelopedAttackVectorSet(),
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[DevelopedAttackVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )

