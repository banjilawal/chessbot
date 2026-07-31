# src/signature/offset/signature.py

"""
Module: signature.signature
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from container import VectorSet
from pattern import Signature

T = TypeVar("T", bound="OffsetRank")

class OffsetSignature(Signature, Generic[T]):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Constraints or that are used to generate a RankTree for Offsetable Ranks; King, knight, Pawn

    Attributes:
        offsets: VectorSet

    Provides:

    Super Class:
        OffsetSignature
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
    
    

    
    