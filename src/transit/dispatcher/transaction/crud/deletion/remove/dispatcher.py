# src/transit/dispatcher/crud/deletion/remove/dispatcher.py

"""
Module: transit.dispatcher.crud.deletion.remove.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import DeletionResult
from operation import NodeRemover
from request import RemoveNodeRequest
from transit import DeletionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="RemoveNodeRequest")

class RemoveNodeDispatcher(DeletionDispatcher[T], ABC, Generic[T]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: NodeRemover[T]
        
    Provides:

    Super Class:
        DeletionDispatcher
    """
    
    def __init__(self, worker: NodeRemover[T]):
        """
        Args:
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        """
        Send RemoveNodeRequests to a worker.
        
        Args:
            request: T
        Result:
            DeletionResult
        Raises:
            RemoveNodeDispatcherException
        """
        pass
