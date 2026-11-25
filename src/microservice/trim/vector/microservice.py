# src/microservice/trim/vector/microservice.py

"""
Module: microservice.trim.vector.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import TrimResult
from collection import VectorChain
from err import VectorChainTrimMicroserviceException
from microservice import ChainTrimMicroservice
from request import VectorChainTrimRequest
from transit import VectorChainTrimDispatcher
from util import LoggingLevelRouter


class VectorChainTrimMicroservice(ChainTrimMicroservice[VectorChainTrimRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the trim-validation security lifecycle.

    Attributes:
        dispatcher: VectorChainTrimDispatcher

    Provides:
        -   def execute(request: VectorChainTrimRequest) -> TrimResult[VectorChain]

    Super Class:
        ChainTrimMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[VectorChainTrimDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorChainTrimDispatcher]
        """
        super().__init__(dispatcher=dispatcher or VectorChainTrimDispatcher())
        
    @property
    def dispatcher(self) -> VectorChainTrimDispatcher:
        return cast(VectorChainTrimDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorChainTrimRequest) -> TrimResult[VectorChain]:
        """
        Handles VectorChainTrimRequests.

        Action:
            1.  Send an exception chain in the TrimResult if the request is
                not fulfilled.
            2.  Otherwise, send the VectorChain in the success result.
        Args:
            request: VectorSearchRequest
        Result:
            TrimResult[VectorChain]
        Raises:
            VectorChainTrimMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            TrimResult.failure(
                VectorChainTrimMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainTrimMicroserviceException.MSG,
                    err_code=VectorChainTrimMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # Handle the case that the trim_context was not found.
        if result.is_nothing_to_trim:
            return TrimResult.nothing_to_trim()
        # --- Forward the work product to the client. ---#
        chain = cast(VectorChain, result.payload)
        return TrimResult.success(chain)
    
    