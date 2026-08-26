# src/transit/dispatcher/builder/pattern/pawn/dispatcher/builder/pattern.py

"""
Module: transit.dispatcher.builder.pattern.pawn.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from topology.pattern import PawnSignature


class AttackSignature(PawnSignature):
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
    
    
