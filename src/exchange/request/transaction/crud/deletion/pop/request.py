# src/exchange/request/transaction/crud/deletion/pop/request.py

"""
Module: exchange.request.transaction.crud.deletion.pop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from artifcat import DeletionResult
from repo.collection import Stack
from domain import Model
from exchange import DeletionRequest

R = TypeVar("R", bound="DeletionResult")
T = TypeVar("T", bound="Model")

class PopRequest(DeletionRequest[R, T], ABC, Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a StackPoper

     Attributes:
         id: int
         item: T
         collection: Stack[T]

     Provides:

     Super Class:
        DeletionRequest
     """
    
    def __init__(self, id: int, item: T, collection: Stack[T]):
        """
        Args:
            id: int
            item: T
            collection: Stack[T]
        """
        super().__init__(id, item=item, collection=collection)
        
    @property
    def item(self) -> T:
        return cast(T, super().item)
    
    @property
    def collection(self) -> Stack[T]:
        return cast(Stack[T], super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PopRequest):
            return self.id == other.id
        return False