# src/request/insertion/chain/request.py

"""
Module: request.insertion.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import cast

from collection import VectorChain
from node import VectorNode
from request import AddNodeRequest


class AddVectorNodeRequest(AddNodeRequest[VectorNode]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the AddNode lifecycle.

     Attributes:
         id: int
         item: T
         chain: Chain[T]

     Provides:
     
     Super Class:
     """
    
    def __init__(self, id: int, item: VectorNode, chain: VectorChain):
        """
        Args:
            id: int
            item: VectorNode
            chain: VectorChain
        """
        super().__init__(id=id, chain=chain, item=item)
        
    @property
    def item(self) -> VectorNode:
        return cast(VectorNode, super().item)
    
    @property
    def collection(self) -> VectorChain:
        return cast(VectorChain, super().collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddVectorNodeRequest):
            request = cast(AddVectorNodeRequest, other)
            return self._id == request.id
        return False