# src/operation/operation.py

"""
Module: operation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from authorization import OperationAuthorizer, OperationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Operation(ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task that produces a Result.

    Attributes:
        authorizer: OperationAuthorizer[T]
        
    Provides:
        -   def execute(request: OperationRequest[T]) -> T

    Super Class:
    """
    _authorizer: OperationAuthorizer[T]
    
    def __init__(self, authorizer: OperationAuthorizer[T]):
        """
        Args:
            authorizer: OperationAuthorizer[T]
        """
        self._authorizer = authorizer
        
        
    @property
    def authorizer(self) -> OperationAuthorizer[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: OperationRequest[T]) -> T:
        """
        Args:
            request: OperationRequest[T]
        Result:
            T
        """
        pass