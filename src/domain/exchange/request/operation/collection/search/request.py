# src/domain/exchange/request/operation/collection/search.request.py

"""
Module: domain.exchange.request.operation.collection.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionRequest
from collection import StackService

from domain.exchange.search.context import Context
from artifcat.result import SearchResult


T = TypeVar("T", bound="StateModel")


class SearchRequest(CollectionRequest[SearchResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the SearchOperation lifecycle.

     Attributes:
        id: int
        context: Context[T]
        stack: StackService[T]
        
     Provides:
     
     Super Class:
        CollectionRequest
     """
    _id: int
    _context: Context[T]
    _stack: StackService[T]

    
    def __init__(self, id: int, context: Context[T], stack: StackService[T],):
        """
        Args:
            id: int
            context: Context[T]
            stack: StackService[T]
        """
        super().__init__(id=id, collectionn=stack)
        self._context = context
        
    @property
    def context(self) -> Context[T]:
        return self._context
    
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            request = cast(SearchRequest, other)
            return self.id == domain.exchange.request.id
        return False