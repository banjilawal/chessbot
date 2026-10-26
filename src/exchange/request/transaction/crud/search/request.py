# src/exchange/request/transaction/crud/search/request.py

"""
Module: exchange.request.transaction.crud.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import SearchResult
from collection import DataStruct
from domain import Context
from exchange import CrudRequest

T = TypeVar("T")

class SearchRequest(CrudRequest[SearchResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide search job details.

     Attributes:
        context: Context[T]
        collection: DataStruct[T]

     Provides:

     Super Class:
        CrudRequest
     """
    
    _context: Context[T]
    _collection: DataStruct[T]
    
    def __init__(
            self,
            id: int,
            context: Context[T],
            collection: DataStruct[T],
    ):
        """
        Args:
            id: int
            context: Context[T]
            collection: DataStruct[T]
        """
        super().__init__(id)
        self._context = context
        self._collection = collection
        
    @property
    def context(self) -> Context[T]:
        return  self._context
    
    @property
    def collection(self) -> DataStruct[T]:
        return self._collection
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            return self.id == other.id
        return False