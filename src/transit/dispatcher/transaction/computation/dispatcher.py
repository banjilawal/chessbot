# src/transit/dispatcher/computation/dispatcher.py

"""
Module: transit.dispatcher.computation.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ComputationResult
from operation import Computer
from request import ComputationRequest
from transit import TransactionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="ComputationRequest")


class ComputationDispatcher(TransactionDispatcher[ComputationResult], ABC, Generic[T]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: ComputationWorker[T]

    Provides:
        -   def  execute(self, request: T) -> ComputationResult

    Super Class:
        TransactionDispatcher
    """
    
    def __init__(self, worker: Computer[T]):
        """
        Args:
            worker: ComputationWorker[T]
        """
        super().__init__(worker=worker)
        
    @property
    def worker(self) -> Computer[T]:
        return cast(Computer[T], super().worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> ComputationResult:
        """
        Distribute ComputationRequests among workers then forward the results.

        Args:
            request: T
        Returns:
            ComputationResult
        Raises:
            ComputationDispatcherException
        """
        pass
