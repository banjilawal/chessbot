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

from authorization import ComputationPermitter, ComputationRequest
from operation import Operator
from artifcat import ComputationResult
from util import LoggingLevelRouter


T = TypeVar("T")


class Computation(Operator[ComputationResult], ABC, Generic[T]):
    """
    Role
        -  Worker

    Responsibilities:
        1.  Execute a task that produces a ComputationResult on success.

    Attributes:
        permitter: ComputationPermitter

    Provides:
        -  execute(request: ComputationRequest) -> ComputationResult

    Super Class:
        Operation
    """
    
    def __init__(self, permitter: ComputationPermitter):
        """
        Args:
            permitter: ComputationPermitter
        """
        super().__init__(permitter=permitter)
    
    @property
    def permitter(self) -> ComputationPermitter:
        return cast(ComputationPermitter, super().permitter)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ComputationRequest) -> ComputationResult[T]:
        pass