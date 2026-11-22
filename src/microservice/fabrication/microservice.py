# src/microservice/fabrication/microservice.py

"""
Module: microservice.fabrication.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import BuildResult
from microservice import Microservice
from request import BuildRequest
from transit import BuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T")


class FabricationMicroservice(Microservice[BuildResult], ABC, Generic[T]):
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
    _dispatcher: BuildDispatcher
    
    def __init__(self, dispatcher: BuildDispatcher):
        """
        Args:
            dispatcher: BuildDispatcher
        """
        super().__init__(dispatcher=dispatcher)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: BuildRequest[T]) -> BuildResult:
        pass
    
    
    