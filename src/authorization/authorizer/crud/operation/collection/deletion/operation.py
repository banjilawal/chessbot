# src/operation/collection/deletion/operation.py

"""
Module: operation.collection.deletion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CollectionDdeletionAuthorizationRequest
from operation import CrudWorker
from artifcat import DeletionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Collection")


class CollectionDeletion(CrudWorker[DeletionResult], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an DeletionResult.

    Attributes:
        authorizer: DeletionAuthorizer[T]
        
    Provides:
        -   def execute(request: DdeletionAuthorizationRequest[T]) -> DeletionResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, authorizer: CollectionDeletionAuthorizer[T]):
        """
        Args:
            authorizer: DeletionAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> CollectionDeletionAuthorizer[T]:
        return cast(CollectionDeletionAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionDdeletionAuthorizationRequest[T]) -> DeletionResult:
        pass