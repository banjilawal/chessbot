# src/domain/exchange/request/crud/search/stack/player/request.py

"""
Module: domain.exchange.request.crud.search.stack.player.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import PlayerStackService
from domain import StackSearchRequest, Player, PlayerSearchContext


class PlayerSearchRequest(StackSearchRequest[Player]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a PlayerStackService and criteria a PlayerSearcher needs to run a job.

     Attributes:
        id: int
        context: PlayerSearchContext
        stack: PlayerStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: PlayerSearchContext, stack: PlayerStackService):
        """
        Args:
            id: int
            context: PlayerSearchContext
            stack: PlayerStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> PlayerSearchContext:
        return cast(PlayerSearchContext, super().context)
        
    @property
    def stack(self) -> PlayerStackService:
        return cast(PlayerStackService, super().stack)
    
    @property
    def collection(self) -> PlayerStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False