# src/space/basis/basis/pawn/attack/opening/space.py

"""
Module: space.basis.basis.pawn.attack.opening.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Vector
from space import VectorTargetingComputer, OpeningAttackVectorSet, PawnAttackVectorBasis


class OpeningPawnAttackVectorBasis(PawnAttackVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destination vectors for a Pawn which has not made its opening move.

    Attributes:
        origin: Vector
        maneuver_vectors: Optional[OpeningAttackVectorSet]
        targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnAttackVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: Optional[OpeningAttackVectorSet] |
                              None = OpeningAttackVectorSet(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: Optional[OpeningAttackVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )

