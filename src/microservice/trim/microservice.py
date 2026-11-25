# src/microservice/trim/microservice.py

"""
Module: microservice.trim.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import TrimResult
from microservice import Microservice
from request import ChainTrimRequest
from transit import ChainTrimDispatcher, Dispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="ChainTrimRequest")


class ChainTrimMicroservice(Microservice[TrimResult], ABC, Generic[T]):
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
        dispatcher: ChainTrimDispatcher[T]

    Provides:
        -   def execute(self, request: T) -> TrimResult

    Super Class:
        Microservice
    """
    
    def __init__(self, dispatcher: ChainTrimDispatcher[T]):
        """
        Args:
            dispatcher: ChainTrimDispatcher
        """
        super().__init__(dispatcher=dispatcher)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> TrimResult:
        """
        Handles ChainTrimRequests.

        Args:
            request: T
        Result:
            TrimResult[hain]
        Raises:
            ChainTrimMicroserviceException
        """
        pass
    
    
    