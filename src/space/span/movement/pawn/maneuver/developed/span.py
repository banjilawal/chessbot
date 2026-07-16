# src/space/span/movement/pawn/space/span.py

"""
Module: space.span.movement.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from model import Vector
from space.span import PawnManeuverVectorSet


class DevelopedManeuverVectorSet(PawnManeuverVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a DevelopedPawnManeuverBasis. Necessary for computing destinations for
            after a PawnToken's first move.

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
    
    
