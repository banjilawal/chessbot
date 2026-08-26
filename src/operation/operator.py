# src/operation/operator.py

"""
Module: operation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from authorization import RequestAuthorizer
from domain import Request
from artifcat import Result
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Operator(ABC, Generic[T]):
    """
    Role
        -  Worker
        -  Result Producer

    Responsibilities:
        1.  Execute a task that produces a Result.

    Attributes:
        authorizer: RequestAuthorizer[T]
        
    Provides:
        -  def execute(request: Request[T]) -> T

    Super Class:
    """
    _authorizer: RequestAuthorizer[T]
    
    def __init__(self, authorizer: RequestAuthorizer[T]):
        """
        Args:
            authorizer: RequestAuthorizer[T]
        """
        self._authorizer = authorizer
        
    @property
    def authorizer(self) -> RequestAuthorizer[T]:
        return self._authorizer
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> T:
        """
        Args:
            request: Request[T]
        Result:
            T
        Raises:
            OperationException
        """
        pass