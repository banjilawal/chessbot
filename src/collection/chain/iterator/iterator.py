# src/collection/chain/iterator/iterator.py

"""
Module: collection.chain.iterator.iterator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import Chain
from domain import Node


class ChainIterator:
    _cursor: Node
    _chain: Chain
    
    def __init__(self, chain: Chain):
        self._chain = chain
        self._cursor = self._chain.head
    
    @property
    def has_next(self,) -> bool:
        return self._cursor.next is not None
    
    def next(self) -> Node:
        next_node = self._cursor.next
        if self.has_next and next_node is not None:
            self._cursor = next_node
            return next_node
        else:
            return self._cursor
            
            
            
    
