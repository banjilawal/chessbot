# src/topology/basis/pawn/attack/developed/basis.py

"""
Module: topology.basis.pawn.attack.developed.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from collection import VectorSet
from schema import Offset
from basis import PawnAttackBasis


class DevelopedPawnAttackBasis(PawnAttackBasis):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Developed attacking Pawns.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnAttackBasis
    """
    def __init__(self, offsets: VectorSet = Offset.DEVELOPED_PAWN_ATTACK.entries,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
