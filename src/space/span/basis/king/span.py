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
from space import DestinationSpanComputer, KingMovementVectorSet, VectorBasis


class KingVectorBasis(VectorBasis[King]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a King by adding it's position to  each
            KingMovementVector.

    Attributes:
            origin: Vector
            movement_vectors: Optional[KingMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[KingMovementVectorSet] |
                              None = KingMovementVectorSet(),
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[KingMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )
