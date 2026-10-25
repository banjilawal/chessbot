# src/operation/collection/insertion/operation.py

"""
Module: operation.collection.insertion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CollectionInsertionPermissionRequest, OperationAuthorizer
from operation import CrudWorker
from artifcat import InsertionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Collection")


class CollectionInsertion(CrudWorker[InsertionResult], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an InsertionResult.

    Attributes:
        authorizer: CollectionInsertionAuthorizer[T]
        
    Provides:
        -   def execute(request: InsertionPermissionRequest[T]) -> InsertionResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, authorizer: CollectionInsertionAuthorizer[T]):
        """
        Args:
            authorizer: CollectionInsertionAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
        
    @property
    def authorizer(self) -> OperationAuthorizer[T]:
        return cast(CollectionInsertionAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionInsertionPermissionRequest[T]) -> InsertionResult:
        pass