# src/transit/dispatcher/crud/dispatcher.py

"""
Module: transit.dispatcher.crud.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import CrudResult
from transit import TransactionDispatcher

T = TypeVar("T", bound="CrudResult")

class CrudDispatcher(TransactionDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute requests among workers then send the result to the correct client

    Attributes:
        worker: CrudWorker[Q, R]

    Provides:
        -   def  execute(self, request: Q) -> R

    Super Class:
        TransactionDispatcher
    """
    
    # def __init__(self, worker: CrudWorker[Q]):
    #     """
    #     Args:
    #         worker: CrudWorker[Q]
    #     """
    #     super().__init__(worker=worker)
    #
    # @property
    # def worker(self) -> CrudWorker[Q]:
    #     return cast(CrudWorker[Q], super().worker)
    #
    # @abstractmethod
    # @LoggingLevelRouter.monitor
    # def execute(self, request: Q) -> R:
    #     """
    #     Distribute CrudRequests among workers then forward the results.
    #
    #     Args:
    #         request: Q
    #     Returns:
    #         R
    #     Raises:
    #         CrudDispatcherException
    #     """
    #     pass
