# src/request/deletion/request.py

"""
Module: request.deletion.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from request import Request
from stack import StackService

T = TypeVar("T")


class DeletionRequest(Request, Generic[T]):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
        1.  Provide information the DeletionPermitter needs to approve or deny removing an item
            from the stack.

     Attributes:
         id: int
         item_id: int
         stack: StackService[T]

     Provides:
        -   def request(id: int, item_id: in, stack: StackService[T]) -> DeletionRequest:

     Super Class:
        Request
     """
    _item_id: int
    _stack: StackService[T]
    
    def __init__(self, id: int, item_id: int, stack: StackService[T]):
        """
         Args:
            id: int
            item_id: int
            stack: StackService[T]
        """
        super().__init__(id=id)
        self._item_id = item_id
        self._stack: stack
    
    @property
    def item_id(self) -> int:
        return self._item_id
    
    @property
    def stack(self) -> StackService[T]:
        return self._stack
    
    @classmethod
    def request(cls, id: int, item_id: int, stack: StackService[T]) -> DeletionRequest:
        return cls(id=id, item_id=item_id, stack=stack)