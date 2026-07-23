# src/space/basis/basis/bishop/space.py

"""
Module: space.basis.basis.bishop.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Bishop, Vector
from space import BishopMovementVector, VectorTargetingComputer, BasisSpace


class BishopBasis(BasisSpace[Bishop]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Bishop by adding it's position to  each
            BishopMovementVector.

    Attributes:
            origin: Vector
            offsets: Optional[BishopVectorSet]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: Optional[BishopMovementVector] |
                              None = BishopMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: Optional[BishopVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )
