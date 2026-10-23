# src/operation/microservice/operation.py

"""
Module: operation.microservice.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from authorization import MicroserviceRequest
from microservice import Microservice
from artifcat import BuildResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="StateModel")


class MicroserviceBuild(Microservice[BuildResult], ABC, Generic[T]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Execute a task on a Microservice that produces either an Build, Deletion, Update
            or Search Result.

    Attributes:
        authorizer: MicroserviceOperationAuthorizer[T]

    Provides:
        -   def execute(request: MicroserviceRequest[T]) -> T

    Super Class:
        Operation
    """
    
    def __init__(self, id: int, authorizer: MicroserviceINAuthorizer[T]):
        """
        Args:
            authorizer: MicroserviceOperationAuthorizer[T]
        """
        super().__init__(id=id, authorizer=authorizer)
    
    @property
    def authorizer(self) -> OperationAuthorizer[T]:
        return cast(MicroserviceOperationAuthorizer[T], super().authorizer)
    
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: MicroserviceRequest[T]) -> T:
        pass