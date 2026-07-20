# src/endpoint/endpoint.py

"""
Module: endpoint.endpoint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from request import DeletionRequest
from result import DeletionResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Endpoint(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: DeletionRequest) -> DeletionResult[T]:
        pass