# src/request/transaction/crud/deletion/pop/request.py

"""
Module: request.transaction.crud.deletion.pop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Stack
from domain import Model, ModelContext
from request import DeletionRequest

T = TypeVar("T", bound="Model")

class PopRequest(DeletionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a StackPoper

     Attributes:
         id: int
         context: ModelContext[T]
         collection: Stack[T]

     Provides:

     Super Class:
        DeletionRequest
     """
    
    def __init__(self, id: int, context: ModelContext[T], collection: Stack[T]):
        """
        Args:
            id: int
            context: ModelContext[T]
            collection: Stack[T]
        """
        super().__init__(id=id, context=context, collection=collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PopRequest):
            return self.id == other.id
        return False