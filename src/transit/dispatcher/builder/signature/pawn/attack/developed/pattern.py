# src/transit/dispatcher/builder/pattern/pawn/dispatcher/builder/pattern.py

"""
Module: transit.dispatcher.builder.pattern.pawn.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from collection import VectorSet
from domain.schema import Offset
from topology.pattern import PawnAttackSignature


class DevelopedPawnAttackPattern(PawnAttackSignature):
    """
    Role:
        - Data Holder
        -  Immutability

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
    
    
