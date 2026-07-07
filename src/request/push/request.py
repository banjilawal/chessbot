# src/request/push/request.py

"""
Module: request.push.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from request import Request
from stack import StackService

T = TypeVar("T")


class PushRequest(Request, Generic[T]):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
         1. Provide information the PushPermitter needs to approve or deny an insertion

     Attributes:
         id: int
         item: T
         stack: StackService[T]

     Provides:
        -   def request(id: int, item: T, stack: StackService[T]) -> PushRequest:

     Super Class:
        Request
     """
    _item: T
    _stack: StackService[T]
    
    def __init__(self, id: int, item: T, stack: StackService[T]):
        """
        Args:
             id: int
             item: T
             stack: StackService[T]
        """
        super().__init__(id=id)
        self._item = item
        self._stack: stack
        
    
    @property
    def item(self) -> T:
        return self._item
    
    @property
    def stack(self) -> StackService[T]:
        return self._stack
    
    @classmethod
    def request(cls, id: int, item: T, stack: StackService[T]) -> PushRequest:
        return cls(id=id, item=item, stack=stack)