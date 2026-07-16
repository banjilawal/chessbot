# src/span/movement/pawn/span.py

"""
Module: span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from model import Pawn
from space.span.movement import MovementVectorSet


class PawnMovementVectorSet(ABC, MovementVectorSet[Pawn]):
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
    
    def __init__(self, movement_vectors: VectorSet):
        """
        Args:
            movement_vectors: VectorSet
        """
        super().__init__(movement_vectors=movement_vectors)
    
