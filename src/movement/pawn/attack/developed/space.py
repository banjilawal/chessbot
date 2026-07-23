# src/space/pawn/space.py

"""
Module: space.pawn.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from schema import Offset
from space import AttackOffsetPattern


class DevelopedAttackOffsetPattern(AttackOffsetPattern):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential attack destinations from a developed Pawn's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        AttackOffsetPattern

    """
    def __init__(self, offsets: VectorSet = Offset.DEVELOPED_PAWN_ATTACK.entries,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
