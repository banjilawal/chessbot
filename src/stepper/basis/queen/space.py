# src/space/basis/basis/queen/space.py

"""
Module: space.basis.basis.queen.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Queen, Vector
from space import VectorTargetingComputer, QueenMovementVector, BasisSpace


class QueenBasis(BasisSpace[Queen]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Queen by adding it's position to  each
            QueenMovementVector.

    Attributes:
            origin: Vector
            offsets: Optional[QueenVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: Optional[QueenMovementVector] |
                              None = QueenMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: Optional[QueenVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )
