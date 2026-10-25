# src/exchange/permissionRequest/permission/crud/search/stack/game/request.py

"""
Module: exchange.request.permission.crud.search.stack.game.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import GameStackService
from exchange import StackSearchPermissionRequest, Game, GameSearchContext


class GameSearchPermissionRequest(StackSearchPermissionRequest[Game]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a GameStackService and criteria a GameSearcher needs to run a job.

     Attributes:
        id: int
        context: GameContext
        stack: GameStackService

     Provides:
     
     Super Class:
        StackSearchPermissionRequest[
     """
    
    def __init__(self, id: int, context: GameSearchContext, stack: GameStackService):
        """
        Args:
            id: int
            context: GameContext
            stack: GameStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> GameSearchContext:
        return cast(GameSearchContext, super().context)
        
    @property
    def stack(self) -> GameStackService:
        return cast(GameStackService, super().stack)
    
    @property
    def collection(self) -> GameStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchPermissionRequest):
            permissionRequest = cast(StackSearchPermissionRequest, other)
            return self.id == permissionRequest.id
        return False