# src/request/operation/collection/deletion/chain.vector.request.py

"""
Module: request.operation.collection.deletion.chain.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from authorization import AddNodeRequest
from collection import VectorChain
from domain.node import VectorNode


class VectorAddNodeRequest(AddNodeRequest[VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the VectorPop lifecycle

     Attributes:
        id: int
        item: Vector
        chain: VectorChain
        
     Provides:
     
     Super Class:
        PopRequest
     """
    
    def __init__(self, id: int, node: VectorNode, chain: VectorChain):
        """
        Args:
            id: int
            item: Vector
            chain: VectorChain
        """
        super().__init__(id=id, node=node, chain=chain)
        
    @property
    def node(self) -> VectorNode:
        return cast(VectorNode, super().node)
    
    @property
    def chain(self) -> VectorChain:
        return cast(VectorChain, super().chain)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorAddNodeRequest):
            request = cast(VectorAddNodeRequest, other)
            return self.id == request.id
        return False