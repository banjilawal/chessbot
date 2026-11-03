# src/exchange/request/transaction/crud/deletion/remove/vector/request.py

"""
Module: exchange.request.transaction.crud.deletion.remove.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import SearchResult
from collection import VectorChain
from domain import VectorNode
from exchange import RemoveNodeRequest

class RemoveVectorNodeRequest(RemoveNodeRequest[SearchResult, VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a VectorNodeRemoveer

     Attributes:
         id: int
         item: VectorNode
         collection: VectorChain

     Provides:

     Super Class:
        RemoveNodeRequest
     """
    
    def __init__(self, id: int, item: VectorNode, collection: VectorChain):
        """
        Args:
            id: int
            item: VectorNode
            collection: VectorChain
        """
        super().__init__(id, item=item, collection=collection)
        
    @property
    def item(self) -> VectorNode:
        return cast(VectorNode, super().item)
    
    @property
    def collection(self) -> VectorChain:
        return cast(VectorChain, super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RemoveVectorNodeRequest):
            return self.id == other.id
        return False