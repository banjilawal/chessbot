# src/transit/dispatcher/crud/insertion/push/dispatcher.py

"""
Module: transit.dispatcher.crud.insertion.push.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import InsertionResult
from operation import ModelPusher
from transit import InsertionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="PushRequest")
R = TypeVar("R", bound="InsertionResult")

class PushDispatcher(InsertionDispatcher[Q, R], ABC, Generic[Q, R]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:
        worker: ModelPusher[Q, R]
        
    Provides:

    Super Class:
        InsertionDispatcher
    """
    
    def __init__(self, worker: ModelPusher[Q, R]):
        """
        Args:
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Send PushRequests to a worker.
        
        Args:
            request: Q
        Result:
            R
        Raises:
            PushDispatcherException
        """
        pass
