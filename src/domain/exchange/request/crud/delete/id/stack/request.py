# src/domain/exchange/request/crud/delete/id/stack/request.py

"""
Module: domain.exchange.request.crud.delete.id.stack.request
Author: Banji Lawal
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import StackService
from domain import DeleteByIdRequest, StateModel


T = TypeVar("T", bound="StateModel")


class PopStackByIdRequest(DeleteByIdRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item_id: int
         collection: StackService[T]

     Provides:
     
     Super Class:
        DeleteByIdRequest
     """
    
    def __init__(self, request_id: int, item_id: int, stack: StackService[T]):
        """
        Args:
            request_id: int
            item_id: int
            stack: StackService[T]
        """
        super().__init__(id=request_id, item_id=item_id, collection=stack)
        
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    @property
    def collection(self) -> StackService[T]:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PopStackByIdRequest):
            request = cast(PopStackByIdRequest, other)
            return self.id == request.id
        return False