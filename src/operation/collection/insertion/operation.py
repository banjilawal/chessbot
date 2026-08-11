# src/operation/collection/insertion/operation.py

"""
Module: operation.collection.insertion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import CollectionInsertionRequest, OperationPermitter
from operation import CollectionOperation
from result import InsertionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Collection")


class CollectionInsertion(CollectionOperation[InsertionResult], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an InsertionResult.

    Attributes:
        permitter: CollectionInsertionPermitter[T]
        
    Provides:
        -   def execute(request: InsertionRequest[T]) -> InsertionResult

    Super Class:
        CollectionOperation
    """
    
    def __init__(self, permitter: CollectionInsertionPermitter[T]):
        """
        Args:
            permitter: CollectionInsertionPermitter[T]
        """
        super().__init__(permitter=permitter)
        
    @property
    def permitter(self) -> OperationPermitter[T]:
        return cast(CollectionInsertionPermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CollectionInsertionRequest[T]) -> InsertionResult:
        pass