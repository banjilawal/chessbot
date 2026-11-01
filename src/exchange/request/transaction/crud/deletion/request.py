# src/exchange/request/transaction/crud/deletion/request.py

"""
Module: exchange.request.transaction.crud.deletion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import DeletionResult
from collection import DataStruct
from exchange import CrudRequest

R = TypeVar("R", bound="DeletionResult")
T = TypeVar("T")

class DeletionRequest(CrudRequest[R, T], ABC, Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide deletion job details.

     Attributes:
         id: int
         item: T
         collection: DataStruct[T]

     Provides:

     Super Class:
        CrudRequest
     """
    _item: T
    _collection: DataStruct[T]
    
    def __init__(self, id: int, item: T, collection: DataStruct[T]):
        """
        Args:
            id: int
            item: T
            collection: DataStruct[T]
        """
        super().__init__(id)
        self._item = item
        self._collection = collection
        
    @property
    def item(self) -> T:
        return self._item
    
    @property
    def collection(self) -> DataStruct[T]:
        return self._collection
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeletionRequest):
            return self.id == other.id
        return False