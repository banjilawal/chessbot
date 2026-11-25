# src/microservice/computation/vector/addition/microservice.py

"""
Module: microservice.computation.vector.addition.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector
from microservice import VectorComputationMicroservice
from request import VectorAdditionRequest
from transit import VectorAdditionDispatcher
from util import LoggingLevelRouter


class VectorAdditionMicroservice(VectorComputationMicroservice[VectorAdditionRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: Optional[VectorAdditionDispatcher]

    Provides:
        -   def execute(request: VectorAdditionRequest) -> ComputationResult[Vector]

    Super Class:
        VectorComputationMicroservice
    """
    
    def __init__(self, dispatcher: Optional[VectorAdditionDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[VectorAdditionDispatcher]
        """
        super().__init__(dispatcher=dispatcher or VectorAdditionDispatcher())
    
    @property
    def dispatcher(self) -> VectorAdditionDispatcher:
        return cast(VectorAdditionDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorAdditionRequest) -> ComputationResult[Vector]:
        """
        Handles RemoveVectorNodeRequests.

        Action:
            1.  Send an exception chain in the ComputationResult if the request is
                not fulfilled.
            2.  Otherwise, send the computation success result.
        Args:
            request: VectorAdditionRequest
        Result:
            ComputationResult[Vector]
        Raises:
            VectorAdditionMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            ComputationResult.failure(
                VectorAdditionMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionMicroserviceException.MSG,
                    err_code=VectorAdditionMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        vector = cast(Vector, result.payload)
        return ComputationResult.success(vector)
    
    
    