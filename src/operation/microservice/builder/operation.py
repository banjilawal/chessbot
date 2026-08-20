# src/operation/microservice/operation.py

"""
Module: operation.microservice.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import MicroserviceRequest
from microservice import Microservice
from result import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="StateModel")


class MicroserviceBuilder(Microservice[BuildResult], ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Microservice that produces either an Build, Deletion, Update
            or Search Result.

    Attributes:
        permitter: MicroserviceOperationPermitter[T]

    Provides:
        -   def execute(request: MicroserviceRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, permitter: MicroserviceBuilderPermitter[T]):
        """
        Args:
            permitter: MicroserviceOperationPermitter[T]
        """
        super().__init__(id=id, permitter=permitter)
    
    @property
    def permitter(self) -> OperationPermitter[T]:
        return cast(MicroserviceOperationPermitter[T], super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: MicroserviceRequest[T]) -> T:
        pass