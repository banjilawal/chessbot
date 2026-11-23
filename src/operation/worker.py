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

from artifcat import TransactionResult
from transit import PermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="TransactionRequest")
R = TypeVar("R", bound="TransactionResult")

class Worker(ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a TransactionRequest

    Attributes:
        permitter: PermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> R

    Super Class:
    """
    _permitter: PermissionDispatcher
    
    def __init__(self, permitter: PermissionDispatcher):
        """
        Args:
            permitter: PermissionDispatcher
        """
        self._permitter = permitter
        
    @property
    def permitter(self) -> PermissionDispatcher:
        return self._permitter
    
    
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