# src/request/transaction/crud/trim/request.py

"""
Module: request.transaction.crud.trim.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import TrimResult
from collection import DataStruct
from domain import Context
from request import CrudRequest

T = TypeVar("T", bound="DataStruct")

class TrimRequest(CrudRequest[TrimResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide trim job details.

     Attributes:
        id: int
        collection: T
        context: Context[T]

     Provides:

     Super Class:
        CrudRequest
     """
    _collection: T
    _context: Context
    
    def __init__(self, id: int, collection: T, context: Context[T]):
        """
        Args:
            id: int
            collection: T
            context: Context
        """
        super().__init__(id)
        self._context = context
        self._collection = collection
    
    @property
    def collection(self) -> T:
        return self._collection
        
    @property
    def context(self) -> Context:
        return self._context
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TrimRequest):
            return self.id == other.id
        return False