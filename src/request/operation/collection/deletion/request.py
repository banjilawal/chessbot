# src/request/operation/collection/deletion.request.py

"""
Module: request.operation.collection.deletion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionRequest
from operation import CollectionDeletion

T = TypeVar("T")
C = TypeVar("C", bound="Collection")


class CollectionDeletionRequest(CollectionRequest[CollectionDeletion], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the DeletionOperation lifecycle.

     Attributes:
        id: int
        item: T
        collection: C
        
     Provides:
     
     Super Class:
        CollectionRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, collection: C):
        """
        Args:
            id: int
            item: T
            collection: C
        """
        super().__init__(id=id, collection=collection)
        self._item = item
        

    @property
    def item(self) -> T:
        return self._item
    
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CollectionDeletionRequest):
            request = cast(CollectionDeletionRequest, other)
            return self.id == request.id
        return False