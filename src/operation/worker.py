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
    Role
        - Worker
        - Result Producer

    Responsibilities:
        1.  Execute a task that produces a Result.

    Attributes:
        authorization_responder: AuthorizationResponder[T]
        
    Provides:
        -   def execute(request: Request[T]) -> T

    Super Class:
    """
    _authorization_responder: AuthorizationResponder
    
    def __init__(self, authorization_responder: AuthorizationResponder):
        """
        Args:
            authorization_responder: AuthorizationResponder
        """
        self._authorization_responder = authorization_responder
        
    @property
    def authorization_responder(self) -> AuthorizationResponder:
        return self._authorization_responder
    
    
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