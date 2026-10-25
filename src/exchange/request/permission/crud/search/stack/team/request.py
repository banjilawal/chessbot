# src/exchange/permissionRequest/permission/crud/search/stack/team/request.py

"""
Module: exchange.request.permission.crud.search.stack.team.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import TeamStackService
from exchange import StackSearchPermissionRequest, Team, TeamSearchContext


class TeamSearchPermissionRequest(StackSearchPermissionRequest[Team]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provide a TeamStackService and criteria a TeamSearcher needs to run a job.

     Attributes:
        id: int
        context: TeamContext
        stack: TeamStackService

     Provides:
     
     Super Class:
        StackSearchPermissionRequest[
     """
    
    def __init__(self, id: int, context: TeamSearchContext, stack: TeamStackService):
        """
        Args:
            id: int
            context: TeamContext
            stack: TeamStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> TeamSearchContext:
        return cast(TeamSearchContext, super().context)
        
    @property
    def stack(self) -> TeamStackService:
        return cast(TeamStackService, super().stack)
    
    @property
    def collection(self) -> TeamStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchPermissionRequest):
            permissionRequest = cast(StackSearchPermissionRequest, other)
            return self.id == permissionRequest.id
        return False