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


class DeletionMicroservice(Microservice[T], ABC, Generic[T]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        id: int
        controller: Controller[T]
        name: Optional[str]

    Provides:

    Super Class:
        Microservice
    """
    
    def __init__(self, dispatcher: DeletionDispatcher):
        """
        Args:
            dispatcher: DeletionDispatcher
        """
        super().__init__(dispatcher=dispatcher)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> DeletionResult:
        pass
    
    
    