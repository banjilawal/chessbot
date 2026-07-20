# src/space/basis/basis/pawn/space.py

"""
Module: space.basis.basis.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, TypeVar

from model import Vector
from space import VectorTargetingComputer, PawnAttackVectorSet, PawnBasis

T = TypeVar("T", bound="PawnAttackVectorSet")


class PawnAttackVectorBasis(ABC, PawnBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Pawn by adding it's position to  each
            PawnMovementVector.

    Attributes:
        origin: Vector
        maneuver_vectors: PawnManeuverVectorSet
        targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: PawnAttackVectorSet[T],
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: PawnManeuverVectorSet
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )
