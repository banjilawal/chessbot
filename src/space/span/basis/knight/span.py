# src/space/span/basis/knight/span.py

"""
Module: space.span.basis.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Knight, Vector
from space import DestinationSpanComputer, KnightMovementVectorSet, VectorBasis


class KnightVectorBasis(VectorBasis[Knight]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Knight by adding it's position to  each
            KnightMovementVector.

    Attributes:
            origin: Vector
            movement_vectors: Optional[KnightMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]      
                  
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[KnightMovementVectorSet] |
                              None = KnightMovementVectorSet(),
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[KnightMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )
