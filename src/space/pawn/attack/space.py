# src/space/pawn/space.py

"""
Module: space.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from space import PawnOffsetPattern
from space.basis import PawnManeuverVector


class PawnAttOffsetPattern(PawnOffsetPattern):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a PawnBasis. They are necessary for computing a PawnToken's
            destination vectors.

    Attributes:
        offsets: DeltaSet

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
    
    
