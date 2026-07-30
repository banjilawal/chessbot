# src/signature/pawn/attack/developed/signature.py

"""
Module: signature.pawn.attack.developed.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from container import VectorSet
from schema import Offset
from signature import PawnAttackSignature


class DevelopedPawnAttackSignature(PawnAttackSignature):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Developed attacking Pawns.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnAttackSignature
    """
    def __init__(self, offsets: VectorSet = Offset.DEVELOPED_PAWN_ATTACK.entries,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
