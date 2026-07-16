# src/span/movement/knight/span.py

"""
Module: span.movement.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import Knight, Vector
from space.span import MovementVectorSet


class KnightMovementVectorSet(MovementVectorSet[Knight]):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfMovement errors by calculating the last point in the direction
            of travel

    Attributes:
        movement_vectors: MovementVectorSet
        
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
                    Vector(1, 2), Vector(-1, 2), Vector(1, -2), Vector(-1, -2),
                    Vector(2, 1), Vector(2, -1), Vector(-2, 1), Vector(-2, -1),
                )
            )
        )
    
