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
from exchange import InsertionRequest
from operation import CrudWorker
from transit import InsertionPermissionDispatcher
from util import LoggingLevelRouter

R = TypeVar("R", bound="InsertionResult")
Q = TypeVar("Q", bound="InsertionRequest")


class Inserter(CrudWorker[R, Q], ABC, Generic[R, Q]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an InsertionRequest

    Attributes:
        dispatcher: InsertionPermissionDispatcher

    Provides:
        -   def execute(request: Q) ->R

    Super Class:
        CrudOperation
    """
    
    def __init__(self, dispatcher: InsertionPermissionDispatcher):
        """
        Args:
            dispatcher: InsertionPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    
    @property
    def dispatcher(self) -> InsertionPermissionDispatcher:
        return cast(InsertionPermissionDispatcher, super().dispatcher)
    
    
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