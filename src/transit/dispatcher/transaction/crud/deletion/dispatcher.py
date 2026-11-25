# src/transit/dispatcher/crud/deleteer/dispatcher.py

"""
Module: transit.dispatcher.crud.deleteer.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import DeletionResult
from operation import Deleter
from request import DeletionRequest
from transit import CrudDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeletionRequest")


class DeletionDispatcher(CrudDispatcher[DeletionResult], ABC, Generic[T]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

    Attributes:
        worker: Deleter[T]
        
    Provides:

    Super Class:
        CrudDispatcher
    """
    
    
    def __init__(self, worker: Deleter[T]):
        """
        Args:
            worker: Deleter[T]
        """
        super().__init__(worker=worker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        pass
