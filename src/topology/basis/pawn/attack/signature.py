# src/topology/basis/pawn/basis.py

"""
Module: topology.basis.pawn.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from container import VectorSet
from basis import PawnBasis


class PawnAttackBasis(PawnBasis, ABC):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Attacking Pawns

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        PawnBasis
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
    
