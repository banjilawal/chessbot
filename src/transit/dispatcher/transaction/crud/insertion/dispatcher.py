# src/transit/dispatcher/crud/inserter/dispatcher.py

"""
Module: transit.dispatcher.crud.inserter.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import InsertionResult
from exchange import InsertionRequest
from operation import Inserter
from transit import CrudDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="InsertionRequest")
R = TypeVar("R", bound="InsertionResult")

class InsertionDispatcher(CrudDispatcher[Q, R], ABC, Generic[Q, R]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: Inserter[Q, R]
        
    Provides:

    Super Class:
        CrudDispatcher
    """
    
    
    def __init__(self, worker: Inserter[Q, R]):
        """
        Args:
            worker: Inserter[Q, R]
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        pass
