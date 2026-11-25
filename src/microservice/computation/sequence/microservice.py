# src/microservice/computation/sequence/microservice.py

"""
Module: microservice.computation.sequence.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from typing import Optional, cast

from artifcat import ComputationResult
from collection import VectorChain
from microservice import ComputationMicroservice
from request import VectorNodeSequenceRequest
from util import LoggingLevelRouter

class VectorNodeSequenceMicroservice(
    ComputationMicroservice[VectorNodeSequenceRequest]
):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the computation-validation security lifecycle.

    Attributes:
        dispatcher: VectorNodeSequenceDispatcher

    Provides:
        -   def execute(request: VectorNodeSequenceRequest) -> ComputationResult

    Super Class:
        ComputationMicroservice
    """
    
    def __init__(self, dispatcher: Optional[VectorNodeSequenceDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[VectorNodeSequenceDispatcher]
        """
        super().__init__(dispatcher=dispatcher)
    
    @property
    def dispatcher(self) -> VectorNodeSequenceDispatcher:
        return cast(VectorNodeSequenceDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorNodeSequenceRequest) -> ComputationResult:
        """
        Handles VectorNodeSequenceRequests.

        Action:
            1.  Send an exception chain in the ComputationResult if the request is
                not fulfilled.
            2.  Otherwise, send the computation success result.
        Args:
            request: VectorNodeSequenceRequest
        Result:
            ComputationResult[VectorChain]
        Raises:
            VectorNodeSequenceMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            ComputationResult.failure(
                VectorNodeSequenceMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSequenceMicroserviceException.MSG,
                    err_code=VectorNodeSequenceMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        chain = cast(VectorChain, result.payload)
        return ComputationResult.success(chain)