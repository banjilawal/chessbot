# src/operation/computation/operation.py

"""
Module: operation.computation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from authorization import ComputationRequest
from operation import Worker
from artifcat import ComputationResult
from util import LoggingLevelRouter


T = TypeVar("T")


class Computation(Worker[ComputationResult], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task that produces a ComputationResult on success.

    Attributes:
        authorizer: ComputationAuthorizer

    Provides:
        - execute(request: ComputationRequest) -> ComputationResult

    Super Class:
        Operation
    """
    
    def __init__(self, authorizer: ComputationAuthorizer):
        """
        Args:
            authorizer: ComputationAuthorizer
        """
        super().__init__(authorizer=authorizer)
    
    @property
    def authorizer(self) -> ComputaionAuthorizer:
        return cast(ComputationAuthorizer, super().authorizer)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ComputationRequest) -> ComputationResult[T]:
        pass