# src/request/pop/request.py

"""
Module: request.pop.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from request import Request
from stack import StackService

T = TypeVar("T")


class PopRequest(Request, Generic[T]):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
         1. Provide information the PopPermitter needs to approve or deny popping the stack.

     Attributes:
         id: int
         stack: StackService[T]

     Provides:
        -   def request(id: int, stack: StackService[T]) -> PopRequest:

     Super Class:
        Request
     """
    _stack: StackService[T]
    
    def __init__(self, id: int, stack: StackService[T]):
        """
        Args:
            id: int
            stack: StackService[T]
        """
        super().__init__(id=id)
        self._stack: stack

    @property
    def stack(self) -> StackService[T]:
        return self._stack
    
    @classmethod
    def request(cls, id: int, stack: StackService[T]) -> PopRequest:
        return cls(id=id, stack=stack)