# src/exchange/request/crud/insertion/push/model/request.py

"""
Module: exchange.request.crud.insertion.push.model.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import ModelStack
from domain import Model
from exchange import PushRequest

T = TypeVar("T", bound="Model")

class ModelPushRequest(PushRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a ModelStackPusher

     Attributes:
         id: int
         item: T
         collection: ModelStack[T]

     Provides:

     Super Class:
        PushRequest
     """
    _item: T
    _collection: ModelStack[T]
    
    def __init__(self, id: int, item: T, collection: ModelStack[T]):
        """
        Args:
            id: int
            item: T
            collection: ModelStack[T]
        """
        super().__init__(id)
        self._item = item
        self._collection = collection
        
    @property
    def item(self) -> T:
        return cast(T, super().item)
    
    @property
    def collection(self) -> ModelStack[T]:
        return cast(ModelStack[T], super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ModelPushRequest):
            return self.id == other.id
        return False