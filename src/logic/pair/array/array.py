# src/logic/pair/array.py

"""
Module: logic.pair.array
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from typing import List

from logic.pair import NodePair


class NodePairList:
    """
    NodePairList's physical structure can be either
    a list or tree.
    """
    _items: List[NodePair]
    
    def __init__(self,):
        self._items = []
        
    @property
    def items(self) -> List[NodePair]:
        return self._items