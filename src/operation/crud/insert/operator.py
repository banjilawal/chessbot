# src/operation/crud/insert/operator.py

"""
Module: operation.crud.insert.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import InsertAuthorizer
from domain import InsertRequest
from operation import CrudOperator
from artifcat.result import InsertionResult
from util import LoggingLevelRouter


T = TypeVar("T", bound="InsertRequest")


class Inserter(CrudOperator[T], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Process an InsertRequest.

    Attributes:
        authorizer: InsertAuthorizer[T]

    Provides:
        -   def execute(self, request: T) -> InsertionResult

    Super Class:
        CrudOperation
    """
    
    def __init__(self, authorizer: InsertAuthorizer[T]):
        """
        Args:
            authorizer: InsertAuthorizer[T]
        """
        super().__init__(authorizer=authorizer)
    
    
    @property
    def authorizer(self) -> InsertAuthorizer[T]:
        return cast(InsertAuthorizer[T], super().authorizer)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> InsertionResult:
        """
        Args:
            request: T
        Result:
            InsertionResult
        Raises:
            InsertException
        """
        pass