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
from model import Pawn
from space import OffsetPattern


class PawnOffsetPattern(ABC, OffsetPattern[Pawn]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a PawnBasis. Necessary for computing a PawnToken's destination vectors.

    Attributes:
        offsets: DeltaSet

    Provides:

    Super Class:
        ManeuverVectorSet
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
