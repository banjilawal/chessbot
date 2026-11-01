# src/exchange/request/transaction/crud/search/node/request.py

"""
Module: exchange.request.transaction.crud.search.node.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import SearchResult
from repo.collection import Chain
from domain import Context, Node
from exchange import SearchRequest

R = TypeVar("R", bound="SearchResult")
T = TypeVar("T", bound="Node")

class NodeSearchRequest(SearchRequest[R, T], ABC, Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a ChainSearcher

     Attributes:
        id: int
        context: Context
        collection: Chain[T]

     Provides:

     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: Context, collection: Chain[T]):
        """
        Args:
            id: int
            context: Context[T]
            collection: Chain[T]
        """
        super().__init__(id=id)
        self._context = context
        self._collection = collection
        
    @property
    def context(self) -> Context:
        return self._context
    
    @property
    def collection(self) -> Chain[T]:
        return self._collection
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            return self.id == other.id
        return False