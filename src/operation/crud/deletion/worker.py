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

from authorization import DeletePermitter
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
        permitter: DeletePermitter[T]

    Provides:
        -   def execute(self, request: T) -> DeletionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, permitter: DeletePermitter[T]):
        """
        Args:
            permitter: DeletePermitter[T]
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> DeletePermitter[T]:
        return cast(DeletePermitter[T], super().permitter)
    
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