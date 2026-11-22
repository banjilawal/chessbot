# src/request/transaction/crud/search/request.py

"""
Module: request.transaction.crud.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Stack
from domain import Context, Model
from request import SearchRequest

T = TypeVar("T", bound="Model")

class ModelSearchRequest(SearchRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to search for a Model

     Attributes:
        id: int
        context: Context[T]
        collection: Stack[T]

     Provides:

     Super Class:
        SearchRequest
     """
    _context: Context[T]
    _collection: Stack[T]
    
    def __init__(self, id: int, context: Context[T], collection: Stack[T]):
        """
        Args:
            id: int
            context: Context[T]
            collection: StackT]
        """
        super().__init__(id=id, context=context, collection=collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SearchRequest):
            return self.id == other.id
        return False