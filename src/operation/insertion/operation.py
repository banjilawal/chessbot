# src/operation/collection/operation.py

"""
Module: operation.collection.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast


from operation import Operation
from result import InsertionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="Collection")


class InsertionOperation(Operation, ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces either an Insertion, Deletion, Update
            or Search Result.

    Attributes:
        authorizer: CollectionOperationAuthorizer[T]
        
    Provides:
        -   def execute(request: CollectionRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, authorizer: InsertionAuthorizer[T]):
        """
        Args:
            authorizer: InsertionAuthorizer[T]
        """
        super().__init__(id=id, authorizer=authorizer)
        
    @property
    def authorizer(self) -> InsertionAuthorizer[T]:
        return cast(InsertionAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: InsertionRequest[T]) -> InsertionResult:
        pass