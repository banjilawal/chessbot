# src/operation/crud/delete/operator.py

"""
Module: operation.crud.delete.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import DeleteDispatcher
from domain import DeleteRequest
from operation import CrudWorker
from artifcat import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeleteRequest")


class Deleter(CrudWorker[DeletionResult], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Process an DeleteRequest.

    Attributes:
        dispatcher: DeleteDispatcher[T]

    Provides:
        -   def execute(self, request: T) -> DeletionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, dispatcher: DeleteDispatcher[T]):
        """
        Args:
            dispatcher: DeleteDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> DeleteDispatcher[T]:
        return cast(DeleteDispatcher[T], super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        """
        Args:
            request: T
        Result:
            DeletionResult
        Raises:
            DeleteException
        """
        pass