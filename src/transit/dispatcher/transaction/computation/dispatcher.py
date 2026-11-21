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
from operation import ComputationWorker
from transit import TransactionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="ComputationRequest")
R = TypeVar("R", bound="ComputationResult")

class ComputationDispatcher(TransactionDispatcher[Q, R], ABC, Generic[Q, R]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: ComputationWorker[Q, R]

    Provides:
        -   def  execute(self, request: Q) -> R

    Super Class:
        TransactionDispatcher
    """
    
    def __init__(self, worker: ComputationWorker[Q, R]):
        """
        Args:
            worker: ComputationWorker[Q, R]
        """
        super().__init__(worker=worker)
        
    @property
    def worker(self) -> ComputationWorker[Q, R]:
        return cast(ComputationWorker[Q, R], super().worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Distribute ComputationRequests among workers then forward the results.

        Args:
            request: Q
        Returns:
            R
        Raises:
            ComputationDispatcherException
        """
        pass
