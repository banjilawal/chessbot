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

from authorization import MicroserviceRequest, OperationAuthorizer
from operation import Operator
from util import LoggingLevelRouter

T = TypeVar("T", bound="Result")


class MicroserviceOperation(Operator, ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Microservice that produces either an Insertion, Deletion, Update
            or Search Result.

    Attributes:
        authorizer: MicroserviceAuthorizer[T]

    Provides:
        -   def execute(request: MicroserviceRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, authorizer: MicroserviceAuthorizer[T]):
        """
        Args:
            authorizer: MicroserviceAuthorizer[T]
        """
        super().__init__(id=id, authorizer=authorizer)
    
    @property
    def authorizer(self) -> OperationAuthorizer[T]:
        return cast(MicroserviceAuthorizer[T], super().authorizer)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: MicroserviceRequest[T]) -> T:
        pass