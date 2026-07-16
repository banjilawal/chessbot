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
from span import PawnManeuverVectorSet


class DevelopedManeuverVectorSet(PawnManeuverVectorSet):
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
        PawnManeuverVectorSet
    """
    
    def __init__(self,):
        """
        """
        super().__init__(
            movement_vectors=VectorSet(
                (Vector(x=0, y=1),)
            )
        )
    
    
