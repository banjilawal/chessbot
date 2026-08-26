# src/domain/exchange/request/crud/search/stack/coord/request.py

"""
Module: domain.exchange.request.crud.search.stack.coord.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import CoordStackService
from domain import StackSearchRequest, Coord, CoordSearchSearchContext


class CoordSearchRequest(StackSearchRequest[Coord]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a CoordStackService and criteria a CoordSearcher needs to run a job.

     Attributes:
        id: int
        context: CoordSearchContext
        stack: CoordStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: CoordSearchSearchContext, stack: CoordStackService):
        """
        Args:
            id: int
            context: CoordSearchContext
            stack: CoordStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> CoordSearchSearchContext:
        return cast(CoordSearchSearchContext, super().context)
        
    @property
    def stack(self) -> CoordStackService:
        return cast(CoordStackService, super().stack)
    
    @property
    def collection(self) -> CoordStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False