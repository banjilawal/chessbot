# src/exchange/permissionRequest/permission/crud/search/stack/board/request.py

"""
Module: exchange.request.permission.crud.search.stack.board.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import BoardStackService
from exchange import StackSearchPermissionRequest, Board, BoardSearchContext


class BoardSearchPermissionRequest(StackSearchPermissionRequest[Board]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a BoardStackService and criteria a BoardSearcher needs to run a job.

     Attributes:
        id: int
        context: BoardContext
        stack: BoardStackService

     Provides:
     
     Super Class:
        StackSearchPermissionRequest[
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
        if isinstance(other, StackSearchPermissionRequest):
            permissionRequest = cast(StackSearchPermissionRequest, other)
            return self.id == permissionRequest.id
        return False