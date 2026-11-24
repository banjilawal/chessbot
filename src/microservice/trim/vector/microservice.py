# src/microservice/trim/vector/microservice.py

"""
Module: microservice.trim.vector.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ChainTrimResult
from collection import VectorChain
from err import VectorChainChainTrimMicroserviceException
from microservice import ChainTrimMicroservice
from request import VectorChainTrimRequest
from transit import VectorChainTrimDispatcher
from util import LoggingLevelRouter


class VectorChainTrimMicroservice(ChainTrimMicroservice[VectorChainTrimRequest]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's trimers and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the trim-validation security lifecycle.

    Attributes:
        dispatcher: Optional[VectorChainTrimDispatcher]

    Provides:

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
    def execute(self, request: VectorChainTrimRequest) -> ChainTrimResult[VectorChain]:
        """
        Handles VectorChainTrimRequests.

        Action:
            1.  Send an exception chain in the PushRequest if the request is
                not fulfilled.
            2.  Otherwise, send the Vector in the success result.
        Args:
            request: VectorSearchRequest
        Result:
            TrimResult[VectorChain]
        Raises:
            VectorChainChainTrimMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        result = self.dispatcher.execute(request)
        if result.is_failure:
            ChainTrimResult.failure(
                VectorChainChainTrimMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorChainChainTrimMicroserviceException.MSG,
                    err_code=VectorChainChainTrimMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        chain = cast(VectorChain, result.payload)
        return ChainTrimResult.success(chain)
    
    