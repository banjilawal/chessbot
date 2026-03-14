# src/logic/pair/listing/listing.py

"""
Module: logic.pair.listing.listing
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.pair import Pair


class PairList:
    """
    PairList's physical structure can be either
    a list or tree.
    """
    _couples: List[Pair]
    
    def __init__(self,):
        self._couples = []
        
    @property
    def couples(self) -> List[Pair]:
        return self._couples
    
    @property
    def is_empty(self) -> bool:
        return len(self._couples) == 0