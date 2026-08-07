# src/authorization/request/stack/request.py

"""
Module: authorization.request.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import TypeVar

from authorization import Request
from stack import StackService

T = TypeVar("T",)

class StackServiceRequest(Request):
    """
    Role:
        -  Request
    
    Responsibilities:
        1. Carry information running a StackService operation.
    
    Attributes:
        id: int
        stack: StackService[T]
    
    Provides:
    
    Super Class:
        Request
    """
    _stack: StackService[T]
    
    def __init__(self, id: int, stack: StackService[T], ):
        """
        Args:
            id: int
            stack: Stack
        """
        super().__init__(id=id)
        self._stack = stack
    
    @property
    def id(self) -> int:
        return super().id
    
    @property
    def stack(self) -> StackService[T]:
        return self._stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackServiceRequest):
            return super().__eq__(other)
        return False
