# src/space/maneuver/pawn/space.py

"""
Module: space.maneuver.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from model import Pawn
from space import ManeuverVectorSet


class PawnManeuverVector(ABC, ManeuverVectorSet[Pawn]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a PawnBasis. Necessary for computing a PawnToken's destination vectors.

    Attributes:
        maneuver_vectors: DeltaSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self, maneuver_vectors: VectorSet):
        """
        Args:
            maneuver_vectors: VectorSet
        """
        super().__init__(maneuver_vectors=maneuver_vectors)
    
