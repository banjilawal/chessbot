# src/microservice/computation/addition.microservice.py

"""
Module: microservice.computation.addition.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from artifcat import ComputationResult
from microservice import DistanceMicroservice
from request import EuclideanDistanceRequest
from util import LoggingLevelRouter


class EuclideanDistanceMicroservice(DistanceMicroservice[EuclideanDistanceRequest]):
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
    
    def __init__(self):
        """
        Args
        """
        super().__init__()

        
    @LoggingLevelRouter.monitor
    def execute(self, request: EuclideanDistanceRequest) -> ComputationResult:
        result = self.dispatcher.execute(request)
        return result
    
    
    