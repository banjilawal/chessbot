# src/signature/pawn/signature.py

"""
Module: signature.pawn.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from model import Pawn
from signature import OffsetSignature


class PawnSignature(ABC, OffsetSignature[Pawn]):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for King

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetSignature
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
