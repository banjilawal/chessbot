# src/authorization/request/operation/collection/insertion/chain.vector.request.py

"""
Module: authorization.request.operation.collection.insertion.chain.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from authorization import AddNodeRequest
from collection import VectorChain
from node import VectorNode


class AddVectorNodeRequest(AddNodeRequest[VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the AddVectorNode lifecycle

     Attributes:
        id: int
        item: VectorNode
        chain: VectorChain
        
     Provides:
     
     Super Class:
        PushRequest
     """
    
    def __init__(self, id: int, item: VectorNode, chain: VectorChain):
        """
        Args:
            id: int
            item: VectorNode
            chain: VectorChain
        """
        super().__init__(id=id, item=item, chain=chain)
        
    @property
    def item(self) -> VectorNode:
        return cast(VectorNode, super().item)
    
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddVectorNodeRequest):
            request = cast(AddVectorNodeRequest, other)
            return self.id == request.id
        return False