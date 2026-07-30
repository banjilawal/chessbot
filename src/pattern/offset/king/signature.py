# src/signature/offset/king/signature.py

"""
Module: signature.offset.king.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from container import VectorSet
from model import King
from schema import Offset
from signature import OffsetSignature


class KingSignature(OffsetSignature[King]):
    """
    Role:
        -   Data Holder
        -   Immutability
        
    Responsibilities:
        1.  Determine potential destinations from KingToken's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetSignature
    """
    
    def __init__(self, offsets: VectorSet = Offset.entries):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
