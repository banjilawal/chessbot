# src/domain/exchange/request/crud/delete/pop/request.py

"""
Module: domain.exchange.request.crud.delete.pop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import StackService
from domain import DeleteItemRequest, StateModel

T = TypeVar("T", bound="StateModel")

class PopStackRequest(DeleteItemRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         collection: StackService[T]

     Provides:
     
     Super Class:
        DeleteItemRequest
     """
    
    def __init__(self, id: int,stack: StackService[T]):
        """
        Args:
            id: int
            stack: StackService[T]
        """
        super().__init__(id=id,  collection=stack)
        
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    @property
    def collection(self) -> StackService[T]:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PopStackRequest):
            request = cast(PopStackRequest, other)
            return self.id == request.id
        return False