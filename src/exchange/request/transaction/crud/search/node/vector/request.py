# src/exchange/request/transaction/crud/search/node/vector/request.py

"""
Module: exchange.request.transaction.crud.search.node.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from repo.collection import VectorChain
from domain import VectorContext, VectorNode
from exchange import NodeSearchRequest


class VectorNodeSearchRequest(NodeSearchRequest[VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to an VectorChainSearcher

     Attributes:
         id: int
         context: VectorContext
         collection: VectorChain

     Provides:

     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: VectorContext, collection: VectorChain):
        """
        Args:
            id: int
            context: VectorContext
            collection: VectorChain
        """
        super().__init__(id, context=context, collection=collection)
        
    @property
    def context(self) -> VectorContext:
        return cast(VectorContext, super().context)
    
    @property
    def collection(self) -> VectorChain:
        return cast(VectorChain, super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeSearchRequest):
            return self.id == other.id
        return False