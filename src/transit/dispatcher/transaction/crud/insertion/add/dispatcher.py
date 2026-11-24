# src/transit/dispatcher/crud/insertion/add/dispatcher.py

"""
Module: transit.dispatcher.crud.insertion.add.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import InsertionResult
from operation import NodeAdder
from request import AddNodeRequest
from transit import InsertionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="AddNodeRequest")

class AddNodeDispatcher(InsertionDispatcher[Q], ABC, Generic[Q]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: NodeAdder[Q]
        
    Provides:

    Super Class:
        InsertionDispatcher
    """
    
    def __init__(self, worker: NodeAdder[Q]):
        """
        Args:
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> InsertionResult:
        """
        Send AddNodeRequests to a worker.
        
        Args:
            request: Q
        Result:
            InsertionResult
        Raises:
            AddDispatcherException
        """
        pass
