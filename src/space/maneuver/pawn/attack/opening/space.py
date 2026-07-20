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
from space.basis import PawnAttackVectorSet


class OpeningAttackVectorSet(PawnAttackVectorSet):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a OpeninfPawnAttackBasis. Necessary for computing a PawnToken's
            attack destination vectors for its first move.

    Attributes:
        maneuver_vectors: VectorSet
        
    Provides:

    Super Class:
        PawnAttackVectorSet
    """
    
    def __init__(self, ):
        """
        """
        super().__init__(
            maneuver_vectors=VectorSet(
                (
                   Vector(x=-1, y=1), Vector(x=1, y=1),
                   Vector(x=-1, y=2), Vector(x=1, y=2),
                )
            )
        )
   
    
    
