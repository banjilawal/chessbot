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

from authorization import OperationPermitter, OperationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Operation(ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task that produces a Result.

    Attributes:
        permitter: OperationPermitter[T]
        
    Provides:
        -   def execute(request: OperationRequest[T]) -> T

    Super Class:
    """
    _permitter: OperationPermitter[T]
    
    def __init__(self, permitter: OperationPermitter[T]):
        """
        Args:
            permitter: OperationPermitter[T]
        """
        self._permitter = permitter
        
        
    @property
    def permitter(self) -> OperationPermitter[T]:
        return self._permitter
    
    
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