# src/transit/dispatcher/dispatcher.py

"""
Module: transit.dispatcher.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import TransactionResult
from exchange import TransactionRequest
from operation import Worker
from transit import Dispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="TransactionRequest")
R = TypeVar("R", bound="TransactionResult")

class TransactionDispatcher(Dispatcher[R], ABC, Generic[Q, R]):
    """
    Role
        -   Performance Management,

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: Worker

    Provides:
        -   def  execute(self, request: Q) -> R

    Super Class:
        Dispatcher
    """
    _worker: Worker
    
    def __init__(self, worker: Worker):
        """
        Args:
            worker: Worker
        """
        self._worker = worker
        
    @property
    def worker(self) -> Worker:
        return self._worker
    
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Distribute TransactionRequests among workers then forward the results.
        
        Args:
            request: Q
        Returns:
            R
        Raises:
            TransactionDispatcherException
        """
        pass