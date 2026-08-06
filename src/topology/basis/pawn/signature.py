# src/topology/basis/pawn/basis.py

"""
Module: topology.basis.pawn.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from collection import VectorSet
from model import Pawn
from basis import OffsetTopologyBasis


class PawnBasis(ABC, OffsetTopologyBasis[Pawn]):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for King

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetTopologyBasis
    """
    
    def __init__(self, offsets: VectorSet):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
