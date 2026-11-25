# src/microservice/deletion/microservice.py

"""
Module: microservice.deletion.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import DeletionResult
from microservice import Microservice
from request import DeletionRequest

from transit import DeletionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="DeletionRequest")


class DeletionMicroservice(Microservice[DeletionResult], ABC, Generic[T]):
    """
    Role:
        -   API
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        dispatcher: DeletionDispatcher[T]

    Provides:
        -   def execute(request: T) -> DeletionResult

    Super Class:
        Microservice
    """
    
    def __init__(self, dispatcher: DeletionDispatcher[T]):
        """
        Args:
            dispatcher: DeletionDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        """
        Handles DeletionRequests.

        Args:
            request: T
        Result:
            DeletionResult
        Raises:
            DeletionMicroserviceException
        """
        pass
    
    
    