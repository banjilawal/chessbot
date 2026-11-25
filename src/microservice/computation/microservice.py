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

T = TypeVar("T", bound="ComputationRequest")


class ComputationMicroservice(Microservice[ComputationResult], ABC, Generic[T]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: ComputationDispatcher[T]

    Provides:
        -   def execute(self, request: T) -> ComputationResult

    Super Class:
        Microservice
    """
    
    def __init__(self, dispatcher: ComputationDispatcher[T]):
        """
        Args:
            dispatcher: ComputationDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
        
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> ComputationResult:
        """
        Handles ComputationRequests.

        Args:
            request: T
        Result:
            ComputationResult
        Raises:
            ComputationMicroserviceException
        """
        pass
    
    
    