# src/span/movement/pawn/span.py

"""
Module: span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from model import Vector
from span import PawnAttackVectorSet


class DevelopedAttackVectorSet(PawnAttackVectorSet):
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
        PawnAttackVectorSet
    """
    
    def __init__(self,):
        """
        Args:
            movement_vectors: MovementVectorSet
        """
        super().__init__(
            movement_vectors=VectorSet(
                (Vector(x=-1, y=1), Vector(x=1, y=1),)
            )
        )
    
    
