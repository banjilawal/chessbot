# src/domain/exchange/request/crud/search/stack/board/request.py

"""
Module: domain.exchange.request.crud.search.stack.board.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import BoardStackService
from domain import StackSearchRequest, Board, BoardSearchContext


class BoardSearchRequest(StackSearchRequest[Board]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a BoardStackService and criteria a BoardSearcher needs to run a job.

     Attributes:
        id: int
        context: BoardContext
        stack: BoardStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: BoardSearchContext, stack: BoardStackService):
        """
        Args:
            id: int
            context: BoardContext
            stack: BoardStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> BoardSearchContext:
        return cast(BoardSearchContext, super().context)
        
    @property
    def stack(self) -> BoardStackService:
        return cast(BoardStackService, super().stack)
    
    @property
    def collection(self) -> BoardStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False