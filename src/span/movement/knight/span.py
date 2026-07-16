# src/span/movement/knight/span.py

"""
Module: span.knight.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Tuple

from container import VectorSet
from model import Knight, Vector
from span import MovementVectorSet


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
    VECTOR_SET: VectorSet =
    
    def __init__(self, movement_vectors=VECTOR_SET):
        """
        Args:
            movement_vectors: MovementVectorSet
        """
        super().__init__(movement_vectors=movement_vectors)
    
