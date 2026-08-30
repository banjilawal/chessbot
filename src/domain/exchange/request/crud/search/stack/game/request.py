# src/domain/exchange/request/crud/search/stack/game/request.py

"""
Module: domain.exchange.request.crud.search.stack.game.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import GameStackService
from domain import StackSearchRequest, Game, GameSearchContext


class GameSearchRequest(StackSearchRequest[Game]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a GameStackService and criteria a GameSearcher needs to run a job.

     Attributes:
        id: int
        context: GameContext
        stack: GameStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
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
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False