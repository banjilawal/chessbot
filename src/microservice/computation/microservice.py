# src/microservice/computation/microservice.py

"""
Module: microservice.computation.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ComputationResult
from microservice import Microservice
from request import ComputationRequest
from transit import ComputationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T")


class ComputationMicroservice(Microservice[ComputationResult], ABC, Generic[T]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's computationers and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        id: int
        controller: Controller[T]
        name: Optional[str]

    Provides:

    Super Class:
        Microservice
    """
    _dispatcher: ComputationDispatcher
    
    def __init__(self, dispatcher: ComputationDispatcher):
        """
        Args:
            dispatcher: ComputationDispatcher
        """
        super().__init__()
        self._dispatcher = dispatcher
        
    @property
    def dispatcher(self) -> ComputationDispatcher:
        return self._dispatcher
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ComputationRequest[T]) -> ComputationResult:
        pass
    
    
    