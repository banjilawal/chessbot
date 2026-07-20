# src/space/span/basis/king/span.py

"""
Module: space.span.basis.king.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import King, Vector
from space import VectorTargetingComputer, KingMovementVector, Basis


class KingBasis(Basis[King]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a King by adding it's position to  each
            KingMovementVector.

    Attributes:
            origin: Vector
            maneuver_vectors: Optional[KingManeuverVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: Optional[KingMovementVector] |
                              None = KingMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: Optional[KingManeuverVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )
