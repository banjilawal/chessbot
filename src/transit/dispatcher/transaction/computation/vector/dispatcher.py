# src/transit/dispatcher/computation/vector/dispatcher.py

"""
Module: transit.dispatcher.computation.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ComputationResult
from request import VectorComputationRequest
from transit import ComputationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="VectorComputationRequest")

class VectorComputationDispatcher(ComputationDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: VectorComputationWorker[T]

    Provides:
        -   def  execute(self, request: T) -> ComputationResult

    Super Class:
        ComputationDispatcher
    """
    
    def __init__(self, worker: VectorComputer[T]):
        """
        Args:
            worker: ComputationWorker[T]
        """
        super().__init__(worker=worker)
    
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
            VectorComputationDispatcherException
        """
        pass
