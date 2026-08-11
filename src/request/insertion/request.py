# src/request/insertion/request.py

"""
Module: request.insertion.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Collection
from operation import InsertionOperation
from request import Request

T = TypeVar("T", bound="Collection")


class InsertionRequest(Request[InsertionOperation], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the InsertionOperation lifecycle.

     Attributes:
         id: int

     Provides:
     
     Super Class:
     """
    _id: int
    _collection: T
    
    def __init__(self, id: int, collection: T):
        """
        Args:
            id: int
            collection: T
        """
        super().__init__(id=id)
        self._collection = collection
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def collection(self) -> T:
        return self._collection
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, InsertionRequest):
            request = cast(InsertionRequest, other)
            return self._id == request.id
        return False