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

from authorization import DeleteAuthorizer
from domain import DeleteRequest
from operation import CrudOperator
from artifcat import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeleteRequest")


class Delete(CrudOperator[T], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Process an DeleteRequest.

    Attributes:
        authorizer: DeleteAuthorizer[T]

    Provides:
        -   def execute(self, request: T) -> DeletionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, authorizer: DeleteAuthorizer[T]):
        """
        Args:
            authorizer: DeleteAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> DeleteAuthorizer[T]:
        return cast(DeleteAuthorizer[T], super().authorizer)
    
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