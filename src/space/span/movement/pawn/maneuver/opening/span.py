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
from space import PawnManeuverVectorSet


class OpeningManeuverVectorSet(PawnManeuverVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a OpeningPawnManeuverBasis. Necessary for computing destinations for
            a PawnToken's first move.

    Attributes:
        movement_vectors: VectorSet

    Provides:

    Super Class:
        PawnManeuverVectorSet
    """
    
    def __init__(self):
        """
        """
        super().__init__(movement_vectors=VectorSet((Vector(x=0, y=1), Vector(x=0, y=2))))
    
    
