# src/request/operation/collection/request.py

"""
Module: request.operation.collection.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import OperationRequest
from collection import Collection
from operation import CollectionOperation

T = TypeVar("T", bound="Result")


class CollectionRequest(OperationRequest[CollectionOperation], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the CollectionOperation lifecycle.

     Attributes:

     Provides:
     
     Super Class:
        OperationRequest
     """
    _collection: Collection
    
    def __init__(self, id: int, collection: Collection):
        """
        Args:
            id: int
            collection: Collection
        """
        super().__init__(id=id)
        self._collection = collection
        
    @property
    def collection(self) -> Collection:
        return self._collection
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CollectionRequest):
            request = cast(CollectionRequest, other)
            return self.id == request.id
        return False