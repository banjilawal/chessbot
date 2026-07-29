# src/builder/pattern/pawn/builder/pattern.py

"""
Module: builder.pattern.pawn.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from model import Pawn
from pattern import OffsetSignature


class PawnOffsetPattern(ABC, OffsetSignature[Pawn]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from PawnToken's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetPattern
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
