# src/exchange/permissionRequest/permission/crud/search/stack/rank/request.py

"""
Module: exchange.request.permission.crud.search.stack.rank.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import RankStackService
from exchange import StackSearchPermissionRequest, Rank, RankContext


class RankSearchPermissionRequest(StackSearchPermissionRequest[Rank]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a RankStackService and criteria a RankSearcher needs to run a job.

     Attributes:
        id: int
        context: RankContext
        stack: RankStackService

     Provides:
     
     Super Class:
        StackSearchPermissionRequest[
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
        if isinstance(other, StackSearchPermissionRequest):
            permissionRequest = cast(StackSearchPermissionRequest, other)
            return self.id == permissionRequest.id
        return False