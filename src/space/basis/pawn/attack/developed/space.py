# src/space/basis/basis/pawn/attack/developed/space.py

"""
Module: space.basis.basis.pawn.attack.developed.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from space import VectorTargetingComputer, DevelopedAttackVectorSet, PawnAttackVectorBasis


class DevelopedPawnAttackVectorBasis(PawnAttackVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors for a Pawn which has not made its developed move.

    Attributes:
        origin: Vector
        maneuver_vectors: Optional[DevelopedAttackVectorSet]
        targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnAttackVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: Optional[DevelopedAttackVectorSet] |
                              None = DevelopedAttackVectorSet(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: Optional[DevelopedAttackVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )

