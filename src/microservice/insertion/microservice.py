# src/microservice/insertion/microservice.py

"""
Module: microservice.insertion.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import InsertionResult
from exchange import InsertionRequest
from transit import InsertionDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="InsertionRequest")


class InsertionMicroservice(ABC, Generic[T]):
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
    _dispatcher: InsertionDispatcher
    
    def __init__(self, dispatcher: InsertionDispatcher):
        """
        Args:
            dispatcher: InsertionDispatcher
        """
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> InsertionDispatcher:
        return self._dispatcher
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> InsertionResult:
        pass
    
    
    