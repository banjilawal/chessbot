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

Q = TypeVar("Q", bound="RemoveNodeRequest")

class RemoveNodeDispatcher(DeletionDispatcher[Q], ABC, Generic[Q]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: NodeRemover[Q]
        
    Provides:

    Super Class:
        DeletionDispatcher
    """
    
    def __init__(self, worker: NodeRemover[Q]):
        """
        Args:
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> DeletionResult:
        """
        Send RemoveNodeRequests to a worker.
        
        Args:
            request: Q
        Result:
            DeletionResult
        Raises:
            RemoveDispatcherException
        """
        pass
