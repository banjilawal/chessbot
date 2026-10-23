# src/operation/collection/insertion/stack/operation.py

"""
Module: operation.collection.insertion.stack.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import StackPushAuthorizer, StackPushRequest
from collection import StackService
from operation import InsertOperation
from artifcat import InsertionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="StateModel")


class StackPush(InsertOperation[StackService], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an InsertionResult.

    Attributes:
        authorizer: PushAuthorizer[T]
        
    Provides:
        -   def execute(request: InsertionRequest[T]) -> InsertionResult

    Super Class:
        InsertionOperation
    """
    
    def __init__(self, authorizer: StackPushAuthorizer[T]):
        """
        Args:
            authorizer: PushAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> StackPushAuthorizer[T]:
        return cast(StackPushAuthorizer[T], super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: StackPushRequest) -> InsertionResult:
        pass