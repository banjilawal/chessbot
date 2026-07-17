# src/space/span/basis/queen/space/span.py

"""
Module: space.span.basis.queen.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from model import Queen, Vector
from space import DestinationSpanComputer, QueenMovementVectorSet, VectorBasis


class QueenVectorBasis(VectorBasis[Queen]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Queen by adding it's position to  each
            QueenMovementVector.

    Attributes:
            origin: Vector
            movement_vectors: Optional[QueenMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[QueenMovementVectorSet] |
                              None = QueenMovementVectorSet(),
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[QueenMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )
