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

from authorization import CollectionDeletionRequest, OperationPermitter
from operation import CrudOperation
from result import DeletionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Collection")


class CollectionDeletion(CrudOperation[DeletionResult], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an DeletionResult.

    Attributes:
        permitter: DeletionPermitter[T]
        
    Provides:
        -   def execute(request: DeletionRequest[T]) -> DeletionResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, permitter: CollectionDeletionPermitter[T]):
        """
        Args:
            permitter: DeletionPermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> CollectionDeletionPermitter[T]:
        return cast(CollectionDeletionPermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionDeletionRequest[T]) -> DeletionResult:
        pass