# src/authorization/request/operation/collection/insertion/stack.request.py

"""
Module: authorization.request.operation.collection.insertion.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionInsertionRequest
from collection import StackService


T = TypeVar("T", bound="StateModel")


class StackPushRequest(CollectionInsertionRequest[StackService], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the StackPush lifecycle.

     Attributes:
        item: T
        stack: StackService[T]

     Provides:
     
     Super Class:
        InsertionRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, stack: StackService[T]):
        """
        Args:
            id: int
            item: T
            stack: StackService[T]
        """
        super().__init__(id=id, collection=stack)
        self._item = item
    
    @property
    def item(self) -> T:
        return self._item
    
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackPushRequest):
            request = cast(StackPushRequest, other)
            return self.id == request.id
        return False