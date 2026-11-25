# src/microservice/computation/vector/multiplication/microservice.py

"""
Module: microservice.computation.vector.multiplication.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Vector
from microservice import ComputationMicroservice
from request import ScalarProductRequest
from transit import ScalarProductDispatcher
from util import LoggingLevelRouter


class ScalarProductMicroservice(VectorComputationMicroservice[ScalarProductRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: Optional[ScalarProductDispatcher]

    Provides:
        -   def execute(self, request: ScalarProductRequest) -> ComputationResult

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
    def execute(self, request: ScalarProductRequest) -> ComputationResult[Vector]:
        """
        Handles RemoveVectorNodeRequests.

        Action:
            1.  Send an exception chain in the ComputationResult if the request is
                not fulfilled.
            2.  Otherwise, send the computation success result.
        Args:
            request: ScalarProductRequest
        Result:
            ComputationResult[Vector]
        Raises:
            ScalarProductMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            ComputationResult.failure(
                ScalarProductMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductMicroserviceException.MSG,
                    err_code=ScalarProductMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        vector = cast(Vector, result.payload)
        return ComputationResult.success(vector)
 
    
    
    