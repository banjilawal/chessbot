# src/domain/exchange/request/crud/search/stack/square/request.py

"""
Module: domain.exchange.request.crud.search.stack.square.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import SquareStackService
from domain import StackSearchRequest, Square, SquareSearchSearchContext


class SquareSearchRequest(StackSearchRequest[Square]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a SquareStackService and criteria a SquareSearcher needs to run a job.

     Attributes:
        id: int
        context: SquareSearchContext
        stack: SquareStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: SquareSearchSearchContext, stack: SquareStackService):
        """
        Args:
            id: int
            context: SquareSearchContext
            stack: SquareStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> SquareSearchSearchContext:
        return cast(SquareSearchSearchContext, super().context)
        
    @property
    def stack(self) -> SquareStackService:
        return cast(SquareStackService, super().stack)
    
    @property
    def collection(self) -> SquareStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False