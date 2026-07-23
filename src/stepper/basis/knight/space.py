# src/space/basis/basis/knight/space.py

"""
Module: space.basis.basis.knight.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Knight, Vector
from space import VectorTargetingComputer, KnightMovementVector, BasisSpace


class KnightBasis(BasisSpace[Knight]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Knight by adding it's position to  each
            KnightMovementVector.

    Attributes:
            origin: Vector
            offsets: Optional[KnightVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]      
                  
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            offsets: Optional[KnightMovementVector] |
                              None = KnightMovementVector(),
            targeting_computer: Optional[VectorTargetingComputer] |
                                None = VectorTargetingComputer(),
    ):
        """
        Args:
            origin: Vector
            offsets: Optional[KnightVectorSet]
            targeting_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            offsets=offsets,
            targeting_computer=targeting_computer,
        )
