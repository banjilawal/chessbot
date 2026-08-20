# src/request/operation/collection/insertion.request.py

"""
Module: request.operation.collection.insertion.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionRequest


from result import InsertionResult


T = TypeVar("T", bound="Collection")


class CollectionInsertionRequest(CollectionRequest[InsertionResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the InsertionOperation lifecycle.

     Attributes:
        id: int
        collection: T
        
     Provides:
     
     Super Class:
        CollectionRequest
     """
    
    def __init__(self, id: int, collection: T):
        """
        Args:
            id: int
            collection: T
        """
        super().__init__(id=id, collection=collection)
        

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CollectionInsertionRequest):
            request = cast(CollectionInsertionRequest, other)
            return self.id == request.id
        return False