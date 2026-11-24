# src/request/transaction/crud/insertion/push/request.py

"""
Module: request.transaction.crud.insertion.push.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Stack
from domain import Model
from request import InsertionRequest

T = TypeVar("T", bound="Model")

class ModelPushRequest(InsertionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a StackPusher

     Attributes:
         id: int
         item: T
         collection: Stack[T]

     Provides:

     Super Class:
        InsertionRequest
     """
    
    def __init__(self, id: int, item: T, collection: Stack[T]):
        """
        Args:
            id: int
            item: T
            collection: Stack[T]
        """
        super().__init__(id=id, item=item, collection=collection)

        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ModelPushRequest):
            return self.id == other.id
        return False