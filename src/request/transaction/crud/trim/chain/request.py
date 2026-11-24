# src/request/transaction/crud/trim/chain/request.py

"""
Module: request.transaction.crud.trim.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from domain import Node, NodeContext
from request import TrimRequest

T = TypeVar("T", bound="Node")

class ChainTrimRequest(TrimRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a NodeChainr

     Attributes:
         id: int
         context: NodeContext[T]
         collection: Chain[T]

     Provides:

     Super Class:
        TrimRequest
     """
    
    def __init__(self, id: int, context: NodeContext[T], collection: Chain[T]):
        """
        Args:
            id: int
            context: NodeContext[T]
            collection: Chain[T]
        """
        super().__init__(id=id, context=context, collection=collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChainTrimRequest):
            return self.id == other.id
        return False