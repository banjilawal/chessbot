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


class PawnManeuverVectorSet(ABC, PawnManeuverVector):
    """
    Role:
        -   Computation Worker
        -   Integrity Management

    Responsibilities:
        1.  Prevent ArrayIndexOutOfManeuver errors by calculating the last point in the direction
            of travel


    Attributes:
        maneuver_vectors: VectorSet
        
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
    
    
