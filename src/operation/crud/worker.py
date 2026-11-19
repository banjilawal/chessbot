# src/operation/crud/worker.py

"""
Module: operation.crud.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import CrudResult
from exchange import CrudRequest
from operation import Worker
from transit import CrudPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("T", bound="CrudRequest")
R = TypeVar("R", bound="CrudResult")

class CrudWorker(Worker[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a CrudRequest

    Attributes:
        dispatcher: CrudPermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        Worker
    """
    
    def __init__(self, dispatcher: CrudPermissionDispatcher):
        """
        Args:
            dispatcher: CrudPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> CrudPermissionDispatcher:
        return cast(CrudPermissionDispatcher, super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            CrudWorkerException
        """
        pass