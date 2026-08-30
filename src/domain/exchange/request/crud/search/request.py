# src/domain/exchange/request/crud/search/request.py

"""
Module: domain.exchange.request.crud.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import CrudRequest, DomainDataObject, Context
from artifcat import SearchResult


T = TypeVar("T", bound="DomainDataObject")


class SearchRequest(CrudRequest[SearchResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         context: SearchContext[T]
         collection: DomainObjectCollection[T]

     Provides:
     
     Super Class:
        CrudRequest
     """
    _context: Context[T]
    
    def __init__(self, id: int, context: Context[T], collection: DomainObjectCollection[T]):
        """
        Args:
            id: int
            context: SearchContext[T]
            collection: DomainObjectCollection[T]
        """
        super().__init__(id=id, collection=collection)
        self._context = context
    
    @property
    def context(self) -> Context[T]:
        return self._context
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            request = cast(SearchRequest, other)
            return self.id == request.id
        return False