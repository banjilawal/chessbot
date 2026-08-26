# src/transit/dispatcher/builder/pattern/pawn/dispatcher/builder/pattern.py

"""
Module: transit.dispatcher.builder.pattern.pawn.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from collection import VectorSet
from domain.model import Pawn
from topology.pattern import OffsetSignature


class PawnOffsetPattern(ABC, OffsetSignature[Pawn]):
    """
    Role:
        -  Data Holder
        -  Immutability

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
    
