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
from domain import VectorNode, VectorNodeContext
from request import ChainTrimRequest


class ChainVectorTrimRequest(ChainTrimRequest[VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a VectorNodeChainer

     Attributes:
         id: int
         context: VectorNodeContext
         collection: VectorChain

     Provides:

     Super Class:
        ChainNodeRequest
     """
    
    def __init__(self, id: int, context: VectorNodeContext, collection: VectorChain):
        """
        Args:
            id: int
            context: VectorNodeContext
            collection: VectorChain
        """
        super().__init__(id=id, context=context, collection=collection)
        
    @property
    def context(self) -> VectorNodeContext:
        return cast(VectorNodeContext, super().context)
    
    @property
    def collection(self) -> VectorChain:
        return cast(VectorChain, super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChainVectorTrimRequest):
            return self.id == other.id
        return False