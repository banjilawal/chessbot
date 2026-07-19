# src/space/span/basis/bishop/span.py

"""
Module: space.span.basis.bishop.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Bishop, Vector
from space import BishopMovementVector, VectorTargetingComputer, Basis


class BishopBasis(Basis[Bishop]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Bishop by adding it's position to  each
            BishopMovementVector.

    Attributes:
            origin: Vector
            maneuver_vectors: Optional[BishopManeuverVectorSet]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            maneuver_vectors: Optional[BishopMovementVector] |
                              None = BishopMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            maneuver_vectors: Optional[BishopManeuverVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            maneuver_vectors=maneuver_vectors,
            targeting_computer=targeting_computer,
        )
