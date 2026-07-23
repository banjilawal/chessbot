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


class PawnManeuverOffsetPattern(ABC, PawnOffsetPattern):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfManeuver errors by calculating the last point in the direction
            of travel


    Attributes:
        offsets: VectorSet
        
    Provides:

    Super Class:
        PawnManeuverVectorSet
    """
    
    def __init__(self, maneuver_vectors: VectorSet):
        """
        Args:
            maneuver_vectors: ManeuverVectorSet
        """
        super().__init__(maneuver_vectors=maneuver_vectors)
    
    
