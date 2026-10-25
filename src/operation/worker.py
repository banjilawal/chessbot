# src/operation/worker.py

"""
Module: operation.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Result
from exchange import AuthorizationResponder, Request
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")

class Worker(ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a TransactionRequest

    Attributes:
        permitter: AuthorizationResponder[T]
        
    Provides:
        -   def execute(request: Request[T]) -> T

    Super Class:
    """
    _permitter: AuthorizationResponder
    
    def __init__(self, permitter: AuthorizationResponder):
        """
        Args:
            permitter: AuthorizationResponder
        """
        self._permitter = permitter
        
    @property
    def permitter(self) -> AuthorizationResponder:
        return self._permitter
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request[T]) -> T:
        """
        Args:
            request: Request[T]
        Result:
            T
        Raises:
            WorkerException
        """
        pass