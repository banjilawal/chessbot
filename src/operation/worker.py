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
Q = TypeVar("Q", bound="TransactionRequest")

class Worker(ABC, Generic[R, Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a TransactionRequest

    Attributes:
        dispatcher: PermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> R

    Super Class:
    """
    _dispatcher: PermissionDispatcher
    
    def __init__(self, dispatcher: PermissionDispatcher):
        """
        Args:
            dispatcher: PermissionDispatcher
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> PermissionDispatcher:
        return self._dispatcher
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            WorkerException
        """
        pass