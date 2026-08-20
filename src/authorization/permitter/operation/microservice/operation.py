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

from authorization import MicroserviceRequest, OperationPermitter
from operation import Operation
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")


class MicroserviceOperation(Operation, ABC, Generic[T]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Execute a task on a Microservice that produces either an Insertion, Deletion, Update
            or Search Result.

    Attributes:
        permitter: MicroservicePermitter[T]

    Provides:
        -   def execute(request: MicroserviceRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, permitter: MicroservicePermitter[T]):
        """
        Args:
            permitter: MicroservicePermitter[T]
        """
        super().__init__(id=id, permitter=permitter)
    
    @property
    def permitter(self) -> OperationPermitter[T]:
        return cast(MicroservicePermitter[T], super().permitter)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: MicroserviceRequest[T]) -> T:
        pass