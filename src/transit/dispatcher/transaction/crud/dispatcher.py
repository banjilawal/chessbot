# src/transit/dispatcher/crud/dispatcher.py

"""
Module: transit.dispatcher.crud.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import CrudResult
from exchange import CrudRequest
from operation import CrudWorker
from transit import Dispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="CrudRequest")
R = TypeVar("R", bound="CrudResult")

class CrudDispatcher(Dispatcher[T], ABC, Generic[Q, R]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:
        worker: CrudWorker[Q, R]

    Provides:

    Super Class:
        Dispatcher
    """
    _worker: CrudWorker[Q, R]
    
    def __init__(self, worker: CrudWorker[Q, R]):
        """
        Args:
            worker: CrudWorker[Q, R]
        """
        super().__init__()
        self._worker = worker
        
    @property
    def worker(self) -> CrudWorker[Q, R]:
        return self._worker
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        pass
