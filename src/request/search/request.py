# src/request/search/request.py

"""
Module: request.search.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from context import Context
from request import Request
from stack import StackService

T = TypeVar("T")


class SearchRequest(Request, Generic[T]):
    """
     Role:
         -  Request
         -  Data Transport

     Responsibilities:
         1. Provide information the SearchPermitter needs to approve or deny an insertion

     Attributes:
         id: int
         context: Context[T]
         stack: StackService[T]

     Provides:
        -   request(cls, id: int, context: Context[T], stack: StackService[T]) -> SearchRequest

     Super Class:
        Request
     """
    _context: Context[T]
    _stack: StackService[T]
    
    def __init__(self, id: int, context: Context, stack: StackService[T]):
        """
        Args:
             id: int
             context: Context[T]
             stack: StackService[T]
        """
        super().__init__(id=id)
        self._context = context
        self._stack: stack
        
    
    @property
    def context(self) -> Context[T]:
        return self._context
    
    @property
    def stack(self) -> StackService[T]:
        return self._stack
    
    @classmethod
    def request(cls, id: int, context: Context[T], stack: StackService[T]) -> SearchRequest:
        return cls(id=id, context=context, stack=stack)