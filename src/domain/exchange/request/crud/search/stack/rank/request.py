# src/domain/exchange/request/crud/search/stack/rank/request.py

"""
Module: domain.exchange.request.crud.search.stack.rank.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import RankStackService
from domain import StackSearchRequest, Rank, RankContext


class RankSearchRequest(StackSearchRequest[Rank]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a RankStackService and criteria a RankSearcher needs to run a job.

     Attributes:
        id: int
        context: RankContext
        stack: RankStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: RankContext, stack: RankStackService):
        """
        Args:
            id: int
            context: RankContext
            stack: RankStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> RankContext:
        return cast(RankContext, super().context)
        
    @property
    def stack(self) -> RankStackService:
        return cast(RankStackService, super().stack)
    
    @property
    def collection(self) -> RankStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False