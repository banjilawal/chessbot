# src/space/span/maneuver/pawn/span.py

"""
Module: space.span.maneuver.pawn.span
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from space.cateoory.basis import PawnManeuverVector


class PawnAttackVectorSet(ABC, PawnManeuverVector):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a PawnBasis. They are necessary for computing a PawnToken's
            destination vectors.

    Attributes:
        maneuver_vectors: DeltaSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self, maneuver_vectors: VectorSet):
        """
        Args:
            maneuver_vectors: ManeuverVectorSet
        """
        super().__init__(maneuver_vectors=maneuver_vectors)
    
    
