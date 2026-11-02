# src/operation/computation/operator.py

"""
Module: operation.computation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import ComputationDispatcher, ComputationRequest
from operation import Worker
from artifcat import ComputationResult
from util import LoggingLevelRouter


T = TypeVar("T")


class Computation(Worker[ComputationResult], ABC, Generic[T]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Execute a task that produces a ComputationResult on success.

    Attributes:
        dispatcher: ComputationDispatcher

    Provides:
        - execute(request: ComputationRequest) -> ComputationResult

    Super Class:
        Operation
    """
    
    def __init__(self, dispatcher: ComputationDispatcher):
        """
        Args:
            dispatcher: ComputationDispatcher
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> ComputationDispatcher:
        return cast(ComputationDispatcher, super().dispatcher)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ComputationRequest) -> ComputationResult[T]:
        pass