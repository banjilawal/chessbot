# src/operation/worker.py

"""
Module: operation.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Self, TypeVar

from artifcat import TransactionResult
from exchange import TransactionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter

R = TypeVar("R", bound="TransactionResult")
T = TypeVar("T", bound="TransactionRequest")

class Worker(ABC, Generic[R, T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a TransactionRequest

    Attributes:
        dispatcher: PermissionDispatcher[T]
        
    Provides:
        -   def execute(request: T) -> R

    Super Class:
    """
    _dispatcher: PermissionDispatcher[T]
    
    def __init__(self, dispatcher: PermissionDispatcher[T]):
        """
        Args:
            dispatcher: PermissionDispatcher
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> PermissionDispatcher[T]:
        return self._dispatcher
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> R:
        """
        Args:
            request: T
        Result:
            R
        Raises:
            WorkerException
        """
        pass