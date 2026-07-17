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
from space import BishopMovementVectorSet, DestinationSpanComputer, VectorBasis


class BishopVectorBasis(VectorBasis[Bishop]):
    """
    Role:
        -   Computation Worker
        -   Integrity Assurance

    Responsibilities:
        1.  Produce a set of destinations for a Bishop by adding it's position to  each
            BishopMovementVector.

    Attributes:
            origin: Vector
            movement_vectors: Optional[BishopMovementVectorSet]
            
    Provides:

    Super Class:
        SpanBasis
    """
    
    def __init__(
            self,
            origin: Vector,
            movement_vectors: Optional[BishopMovementVectorSet] | None = BishopMovementVectorSet(),
            destination_span_computer: Optional[DestinationSpanComputer] |
                                       None = DestinationSpanComputer(),
    ):
        """
        Args:
            origin: Vector
            movement_vectors: Optional[BishopMovementVectorSet]
            destination_span_computer: Optional[DestinationSpanComputer]
        """
        super().__init__(
            origin=origin,
            movement_vectors=movement_vectors,
            destination_span_computer=destination_span_computer,
        )
