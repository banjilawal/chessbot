# src/span/movement/king/span.py

"""
Module: span.movement.king.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import King, Vector
from span import MovementVectorSet


class KingMovementVectorSet(MovementVectorSet[King]):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfMovement errors by calculating the last point in the direction
            of travel

    Attributes:
        movement_vectors: VectorSet
        
    Provides:

    Super Class:
        MovementVectorSet
    """
    
    def __init__(self,):
        """
        Args:t
        """
        super().__init__(
            movement_vectors=VectorSet(
                    (
                        Vector(1, 0), Vector(-1, 0), Vector(0, 1),
                        Vector(1, 1), Vector(-1, 1), Vector(-1, -1), Vector(1, -1)
                    )
            )
        )
    
