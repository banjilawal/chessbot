# src/operation/crud/insertion/worker.py

"""
Module: operation.crud.insertion.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import InsertionResult
from operation import CrudWorker
from request import InsertionRequest
from transit import InsertionPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("Q", bound="InsertionRequest")
R = TypeVar("R")



class Inserter(CrudWorker[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an InsertionRequest

    Attributes:
        permitter: InsertionPermissionDispatcher

    Provides:
        -   def execute(request: Q) ->R

    Super Class:
        CrudOperation
    """
    
    def __init__(self, permitter: InsertionPermissionDispatcher):
        """
        Args:
            permitter: InsertionPermissionDispatcher
        """
        super().__init__(permitter=permitter)
    
    
    @property
    def permitter(self) -> InsertionPermissionDispatcher:
        return cast(InsertionPermissionDispatcher, super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> InsertionResult:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            InserterException
        """
        pass