# src/exchange/request/crud/insertion/push/request.py

"""
Module: exchange.request.crud.insertion.push.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Stack
from exchange import CrudRequest, InsertionRequest

T = TypeVar("T")

class PushRequest(InsertionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a StackPusher

     Attributes:
         id: int
         item: T
         collection: Stack[T]

     Provides:

     Super Class:
        InsertionRequest
     """
    _item: T
    _collection: Stack[T]
    
    def __init__(self, id: int, item: T, collection: Stack[T]):
        """
        Args:
            id: int
            item: T
            collection: Stack[T]
        """
        super().__init__(id)
        self._item = item
        self._collection = collection
        
    @property
    def item(self) -> T:
        return self._item
    
    @property
    def collection(self) -> Stack[T]:
        return self._collection
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PushRequest):
            return self.id == other.id
        return False