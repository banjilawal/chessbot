# src/request/transaction/crud/trim/chain/vector/request.py

"""
Module: request.transaction.crud.trim.chain.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import VectorChain
from domain import VectorNodeContext
from request import ChainTrimRequest


class VectorChainTrimRequest(ChainTrimRequest[VectorChain]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a VectorNodeChainer

     Attributes:
        id: int
        collection: VectorChain
        context: VectorNodeContext

     Provides:

     Super Class:
        ChainNodeRequest
     """
    
    def __init__(self, id: int, collection: VectorChain, context: VectorNodeContext):
        """
        Args:
            id: int
            collection: VectorChain
            context: VectorNodeContext
        """
        super().__init__(id=id, collection=collection, context=context)
    
    @property
    def collection(self) -> VectorChain:
        return cast(VectorChain, super().collection)
        
    @property
    def context(self) -> VectorNodeContext:
        return cast(VectorNodeContext, super().context)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorChainTrimRequest):
            return self.id == other.id
        return False