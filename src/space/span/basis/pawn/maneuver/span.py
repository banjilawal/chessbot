# src/space/span/basis/pawn/span.py

"""
Module: space.span.basis.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, TypeVar

from model import Vector
from space import DestinationSpanComputer, PawnManeuverVectorSet, PawnVectorBasis

T = TypeVar("T", bound="PawnManeuverVectorSet")


class PawnManeuverVectorBasis(ABC, PawnVectorBasis):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Pawn by adding it's position to  each
            PawnMovementVector.

    Attributes:
        origin: Vector
        movement_vectors: PawnMovementVectorSet
        destination_span_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        PawnVectorBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: PawnManeuverVectorSet[T],
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: PawnMovementVectorSet
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )
