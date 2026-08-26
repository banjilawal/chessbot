# src/domain/exchange/request/crud/search/stack/arena/request.py

"""
Module: domain.exchange.request.crud.search.stack.arena.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import ArenaStackService
from domain import StackSearchRequest, Arena, ArenaSearchSearchContext


class ArenaSearchRequest(StackSearchRequest[Arena]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a ArenaStackService and criteria a ArenaSearcher needs to run a job.

     Attributes:
        id: int
        context: ArenaSearchContext
        stack: ArenaStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: ArenaSearchSearchContext, stack: ArenaStackService):
        """
        Args:
            id: int
            context: ArenaSearchContext
            stack: ArenaStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> ArenaSearchSearchContext:
        return cast(ArenaSearchSearchContext, super().context)
        
    @property
    def stack(self) -> ArenaStackService:
        return cast(ArenaStackService, super().stack)
    
    @property
    def collection(self) -> ArenaStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False