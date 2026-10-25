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
from transit import CrudPermissionPermitter
from util import LoggingLevelRouter

T = TypeVar("T", bound="CrudResult")


class CrudWorker(Worker[T], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a CrudRequest

    Attributes:
        permitter: CrudPermissionPermitter[T]
        
    Provides:
        -   def execute(request: CrudRequest[T]) -> T

    Super Class:
        Worker
    """
    
    def __init__(self, permitter: CrudPermissionPermitter[T]):
        """
        Args:
            permitter: CrudPermissionPermitter[T]
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> CrudPermissionPermitter[T]:
        return cast(CrudPermissionPermitter[T], super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: CrudRequest[T]) -> T:
        """
        Args:
            request: CrudRequest[T]
        Result:
            T
        Raises:
            CrudWorkerException
        """
        pass