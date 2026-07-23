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

from space import VectorTargetingComputer, PawnMovementVector, BasisSpace

T = TypeVar("T", bound="PawnVectorSet")

from model import Pawn, Vector



class PawnBasis(ABC, BasisSpace[Pawn]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Pawn by adding it's position to  each
            PawnMovementVector.

    Attributes:
            origin: Vector
            offsets: PawnVectorSet
            targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: PawnMovementVector[T],
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: PawnVectorSet
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )
