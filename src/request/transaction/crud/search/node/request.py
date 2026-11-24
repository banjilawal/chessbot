# src/request/transaction/crud/search/node/request.py

"""
Module: request.transaction.crud.search.node.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Chain
from domain import Node, NodeContext
from request import SearchRequest

T = TypeVar("T", bound="Node")

class NodeSearchRequest(SearchRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a ChainSearcher

     Attributes:
        id: int
        context: Context[T]
        collection: Chain[T]

     Provides:

     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: NodeContext[T], collection: Chain[T]):
        """
        Args:
            id: int
            context: Context[T]
            collection: Chain[T]
        """
        super().__init__(id=id)
        self._context = context
        self._collection = collection

        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            return self.id == other.id
        return False