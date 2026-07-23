# src/space/pawn/space.py

"""
Module: space.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from space import PawnOffsetPattern


class AttackOffsetPattern(PawnOffsetPattern):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential attack destinations from PawnToken's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnOffsetPattern
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
