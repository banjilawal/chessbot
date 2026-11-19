# src/transit/dispatcher/attack/pattern/offset/king/dispatcher/attack/pattern.py

"""
Module: transit.dispatcher.attack.pattern.offset.king.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from domain.model import King
from domain.schema import Offset
from surface.topology import OffsetSignature


class KingOffsetPattern(OffsetSignature[King]):
    """
    Role:
        - Data Holder
        - Immutability
        
    Responsibilities:
        1.  Determine potential destinations from KingToken's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetPattern
    """
    
    def __init__(self, offsets: VectorSet = Offset.entries):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
