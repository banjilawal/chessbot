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
        permitter: DeletePermitter

    Provides:
        -   def execute(request: Q) -> DeletionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, permitter: DeletePermitter):
        """
        Args:
            permitter: DeletePermitter
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> DeletePermitter:
        return cast(DeletePermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> DeletionResult:
        """
        Args:
            request: Q
        Result:
            DeletionResult
        Raises:
            DeleteException
        """
        pass