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
from signature import PawnSignature


class PawnAttackSignature(PawnSignature, ABC):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Attacking Pawns

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnSignature
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
