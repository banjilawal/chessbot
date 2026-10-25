# src/exchange/permissionRequest/permission/crud/search/stack/arena/request.py

"""
Module: exchange.request.permission.crud.search.stack.arena.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import ArenaStackService
from exchange import StackSearchPermissionRequest, Arena, ArenaSearchContext


class ArenaSearchPermissionRequest(StackSearchPermissionRequest[Arena]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a ArenaStackService and criteria a ArenaSearcher needs to run a job.

     Attributes:
        id: int
        context: ArenaContext
        stack: ArenaStackService

     Provides:
     
     Super Class:
        StackSearchPermissionRequest[
     """
    
    def __init__(self, id: int, context: ArenaSearchContext, stack: ArenaStackService):
        """
        Args:
            id: int
            context: ArenaContext
            stack: ArenaStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> ArenaSearchContext:
        return cast(ArenaSearchContext, super().context)
        
    @property
    def stack(self) -> ArenaStackService:
        return cast(ArenaStackService, super().stack)
    
    @property
    def collection(self) -> ArenaStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchPermissionRequest):
            permissionRequest = cast(StackSearchPermissionRequest, other)
            return self.id == permissionRequest.id
        return False