# src/space/span/basis/rook/span.py

"""
Module: space.span.basis.rook.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Rook, Vector
from space import VectorTargetingComputer, RookMovementVector, BasisSpace


class RookBasis(BasisSpace[Rook]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Rook by adding it's position to  each
            RookMovementVector.

    Attributes:
            origin: Vector
            maneuver_vectors: Optional[RookManeuverVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: Optional[RookMovementVector] |
                              None = RookMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: Optional[RookManeuverVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )
