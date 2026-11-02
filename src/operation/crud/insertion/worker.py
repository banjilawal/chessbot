# src/operation/crud/insertion/worker.py

"""
Module: operation.crud.insertion.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import InsertionResult
from exchange import InsertionRequest
from operation import CrudWorker
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionRequest")


class Inserter(CrudWorker[InsertionResult], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an InsertionRequest

    Attributes:
        dispatcher: InsertionPermissionDispatcher[T]

    Provides:
        -   def execute(self, request: T) -> InsertionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, dispatcher: PushPermissionDispatcher[T]):
        """
        Args:
            dispatcher: InsertionPermissionDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher[T])
    
    
    @property
    def dispatcher(self) -> PushPermissionDispatcher[T]:
        return cast(PushPermissionDispatcher[T], super().dispatcher)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> InsertionResult:
        """
        Args:
            request: T
        Result:
            InsertionResult
        Raises:
            InserterException
        """
        pass