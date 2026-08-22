# src/topology/basis/offset/knight/basis.py

"""
Module: topology.basis.offset.knight.basis
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from domain.model import Knight

from domain.schema import Offset


class KnightTopologyBasis(OffsetTopologyBasis[Knight]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from a Knight's current position.

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetTopologyBasis
    """
    
    def __init__(self,  offsets: VectorSet = Offset.KNIGHT.entries):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__(offsets=offsets)
    
