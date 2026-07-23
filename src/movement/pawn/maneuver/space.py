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


class ManeuverOffsetPattern(ABC, PawnOffsetPattern):
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
        PawnVectorSet
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
