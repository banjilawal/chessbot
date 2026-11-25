# src/microservice/computation/vector/addition.microservice.py

"""
Module: microservice.computation.vector.addition.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ComputationResult
from domain import Scalar
from microservice import ComputationMicroservice
from request import EuclideanDistanceRequest
from transit import DistanceDispatcher
from util import LoggingLevelRouter


class EuclideanDistanceMicroservice(ComputationMicroservice[EuclideanDistanceRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: Optional[EuclideanDistanceDispatcher]

    Provides:
        -   def execute(request: EuclideanDistanceRequest) -> ComputationResult[Scalar]

    Super Class:
        ComputationMicroservice
    """
    
    def __init__(self, dispatcher: Optional[DistanceDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[EuclideanDistanceDispatcher]
        """
        super().__init__(dispatcher=dispatcher or DistanceDispatcher())
    
    @property
    def dispatcher(self) -> DistanceDispatcher:
        return cast(DistanceDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: EuclideanDistanceRequest) -> ComputationResult[Scalar]:
        """
        Handles EuclideanDistanceRequests.

        Action:
            1.  Send an exception chain in the ComputationResult if the request is
                not fulfilled.
            2.  Otherwise, send the computation success result.
        Args:
            request: EuclideanDistanceRequest
        Result:
            ComputationResult[Scalar]
        Raises:
            EuclideanDistanceMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            ComputationResult.failure(
                EuclideanDistanceMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EuclideanDistanceMicroserviceException.MSG,
                    err_code=EuclideanDistanceMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        scalar = cast(Scalar, result.payload)
        return ComputationResult.success(scalar)
    
    