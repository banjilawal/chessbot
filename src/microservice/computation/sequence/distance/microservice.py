# src/microservice/computation/vector/distance/microservice.py

"""
Module: microservice.computation.vector.distance.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import ComputationResult
from domain import Scalar
from microservice import VectorComputationMicroservice
from request import DistanceRequest
from transit import DistanceDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="DistanceRequest")


class DistanceMicroservice(VectorComputationMicroservice[T], ABC, Generic[T]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: DistanceDispatcher[T]

    Provides:
        -   def execute(request: T) -> ComputationResult[Scalar]

    Super Class:
        VectorComputationMicroservice
    """
    
    def __init__(self, dispatcher: DistanceDispatcher[T]):
        """
        Args:
            dispatcher: DistanceDispatcher[T]
        """
        super().__init__(dispatcher=dispatcher)
 
    
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> ComputationResult[Scalar]:
        """
        Handles DistanceRequests.

        Args:
            request: T
        Result:
            ComputationResult[Scalar]
        Raises:
            DistanceMicroserviceException
        """
        pass