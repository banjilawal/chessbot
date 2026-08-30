# src/domain/exchange/request/crud/search/stack/snapshot/request.py

"""
Module: domain.exchange.request.crud.search.stack.snapshot.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import SnapshotStackService
from domain import StackSearchRequest, Snapshot, SnapshotContext


class SnapshotSearchRequest(StackSearchRequest[Snapshot]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a SnapshotStackService and criteria a SnapshotSearcher needs to run a job.

     Attributes:
        id: int
        context: SnapshotContext
        stack: SnapshotStackService

     Provides:
     
     Super Class:
        StackSearchRequest[
     """
    
    def __init__(self, id: int, context: SnapshotContext, stack: SnapshotStackService):
        """
        Args:
            id: int
            context: SnapshotContext
            stack: SnapshotStackService
        """
        super().__init__(id=id, context=context, stack=stack)
        
    @property
    def context(self) -> SnapshotContext:
        return cast(SnapshotContext, super().context)
        
    @property
    def stack(self) -> SnapshotStackService:
        return cast(SnapshotStackService, super().stack)
    
    @property
    def collection(self) -> SnapshotStackService:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False