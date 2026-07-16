# src/space/span/movement/pawn/space/span.py

"""
Module: space.span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from space.span import PawnMovementVectorSet


class PawnManeuverVectorSet(ABC, PawnMovementVectorSet):
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
        PawnMovementVectorSet
    """
    
    def __init__(self, movement_vectors: VectorSet):
        """
        Args:
            movement_vectors: MovementVectorSet
        """
        super().__init__(movement_vectors=movement_vectors)
    
    
