# src/domain/exchange/request/crud/delete/item/stack/request.py

"""
Module: domain.exchange.request.crud.delete.item.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import StackService
from domain import DeleteItemRequest, StatefulModel

T = TypeVar("T", bound="StatefulModel")

class DeleteStackItemRequest(DeleteItemRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item: T
         collection: StackService[T]

     Provides:
     
     Super Class:
        DeleteItemRequest
     """
    
    def __init__(self, id: int, item: T, stack: StackService[T]):
        """
        Args:
            id: int
            item: T
            stack: StackService[T]
        """
        super().__init__(id=id, item=item, collection=stack)
    
    @property
    def item(self) -> T:
        return cast(T, super().item)
        
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    @property
    def collection(self) -> StackService[T]:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeleteStackItemRequest):
            request = cast(DeleteStackItemRequest, other)
            return self.id == request.id
        return False