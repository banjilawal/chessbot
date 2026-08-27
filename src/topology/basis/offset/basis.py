# src/topology/basis/offset/basis.py

"""
Module: topology.basis.basis
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import VectorSet
from topology.pattern import TopologyBasis

T = TypeVar("T", bound="OffsetRank")

class OffsetTopologyBasis(TopologyBasis, ABC, Generic[T]):
    """
    Role:
        - Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Offsetable Ranks; King, knight, Pawn

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetTopologyBasis
    """
    _offsets: VectorSet
    
    def __init__(self, offsets: VectorSet,):
        """
        Args:
            offsets: VectorSet
        """
        super().__init__()
        self._offsets = offsets
        
    @property
    def offsets(self) -> VectorSet:
        return self._offsets
    
    

    
    