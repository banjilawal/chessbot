# src/space/maneuver/pawn/space.py

"""
Module: space.maneuver.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from model import Vector
from space.basis import PawnManeuverVectorSet


class DevelopedManeuverVectorSet(PawnManeuverVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a DevelopedPawnManeuverBasis. Necessary for computing destinations for
            after a PawnToken's first move.

    Attributes:
        maneuver_vectors: VectorSet

    Provides:

    Super Class:
        PawnManeuverVectorSet
    """
    
    def __init__(self,):
        """
        """
        super().__init__(
            maneuver_vectors=VectorSet(
                (Vector(x=0, y=1),)
            )
        )
    
    
