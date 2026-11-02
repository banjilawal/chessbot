# src/operation/crud/insertion/stack/operator.py

"""
Module: operation.crud.insertion.stack.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import StackPushDispatcher, StackPushRequest
from repo.collection import StackService
from operation import InsertionOperation
from artifcat import InsertionionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="StateModel")


class StackPusher(InsertionOperation[StackService], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Execute a task on a Collection that produces an InsertionionResult.

    Attributes:
        dispatcher: PushDispatcher[T]
        
    Provides:
        -   def execute(request: InsertionionRequest[T]) -> InsertionionResult

    Super Class:
        InsertionionOperation
    """
    
    def __init__(self, dispatcher: StackPushDispatcher[T]):
        """
        Args:
            dispatcher: PushDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> StackPushDispatcher[T]:
        return cast(StackPushDispatcher[T], super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: StackPushRequest) -> InsertionionResult:
        pass