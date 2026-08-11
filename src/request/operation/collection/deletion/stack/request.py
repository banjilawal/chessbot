# src/request/operation/collection/deletion/stack.request.py

"""
Module: request.operation.collection.deletion.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionDeletionRequest
from collection import StackService


T = TypeVar("T", bound="StateModel")


class StackPopRequest(CollectionDeletionRequest[StackService], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the StackPop lifecycle.

     Attributes:
        item: T
        stack: StackService[T]

     Provides:
     
     Super Class:
        DeletionRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, stack: StackService[T]):
        """
        Args:
            id: int
            item_id: int
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
        if isinstance(other, StackPopRequest):
            request = cast(StackPopRequest, other)
            return self.id == request.id
        return False