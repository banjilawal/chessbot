# src/operation/computation/worker.py

"""
Module: operation.computation.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ComputationResult
from exchange import ComputationRequest
from operation import Worker
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter

Q = TypeVar("T", bound="ComputationRequest")
R = TypeVar("R", bound="ComputationResult")

class ComputationWorker(Worker[Q, R], ABC, Generic[Q, R]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes a ComputationRequest

    Attributes:
        dispatcher: ComputationPermissionDispatcher
        
    Provides:
        -   def execute(request: Q) -> R

    Super Class:
        Worker
    """
    
    def __init__(self, dispatcher: ComputationPermissionDispatcher):
        """
        Args:
            dispatcher: ComputationPermissionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> ComputationPermissionDispatcher:
        return cast(ComputationPermissionDispatcher, super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Q) -> R:
        """
        Args:
            request: Q
        Result:
            R
        Raises:
            ComputationWorkerException
        """
        pass