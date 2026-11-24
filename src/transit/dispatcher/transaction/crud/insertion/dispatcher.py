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
from operation import Inserter
from request import InsertionRequest
from transit import CrudDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="InsertionRequest")


class InsertionDispatcher(CrudDispatcher[Q], ABC, Generic[Q]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: Inserter[Q]
        
    Provides:

    Super Class:
        CrudDispatcher
    """
    
    
    def __init__(self, worker: Inserter[Q]):
        """
        Args:
            worker: Inserter[Q]
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> InsertionResult:
        pass
