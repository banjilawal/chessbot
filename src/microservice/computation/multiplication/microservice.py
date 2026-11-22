# src/microservice/computation/multiplication/microservice.py

"""
Module: microservice.computation.multiplication.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from microservice import ComputationMicroservice
from request import ScalarProductRequest
from transit import ScalarProductDispatcher
from util import LoggingLevelRouter


class ScalarProductMicroservice(ComputationMicroservice[ScalarProductRequest]):
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
    
    def __init__(self, dispatcher: Optional[ScalarProductDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[ScalarProductDispatcher]
        """
        super().__init__(dispatcher=dispatcher or ScalarProductDispatcher())

        
    @property
    def dispatcher(self) -> ScalarProductDispatcher:
        return cast(ScalarProductDispatcher, super().dispatcher)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: ScalarProductRequest) -> ComputationResult:
        result = self.dispatcher.execute(request)
        return result
    
    
    