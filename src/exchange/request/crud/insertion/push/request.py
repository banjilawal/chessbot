# src/exchange/request/crud/insertion/push/request.py

"""
Module: exchange.request.crud.insertion.push.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


T = TypeVar("T", bound="Model")

class PushRequest(InsertionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a StackPusher

     Attributes:
         id: int
         item: T
         stack: Stack[T]

     Provides:

     Super Class:
        InsertionRequest
     """
    
    def __init__(self, id: int, item: T, stack: ModelStack[T]):
        """
        Args:
            id: int
            item:
        """
        super().__init__(id)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CrudRequest):
            return self.id == request.id
        return False