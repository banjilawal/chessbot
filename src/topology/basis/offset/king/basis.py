# src/topology/basis/offset/king/basis.py

"""
Module: topology.basis.offset.king.basis
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from collection import VectorSet
from model import King

from schema import Offset


class KingTopologyBasis(OffsetTopologyBasis[King]):
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
    
    def __init__(self, offsets: VectorSet = Offset.KING.entries):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
