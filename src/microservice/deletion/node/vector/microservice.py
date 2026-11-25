# src/microservice/deletion/node/vector/microservice.py

"""
Module: microservice.deletion.node.vector.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import DeletionResult
from domain import VectorNode
from err import VectorNodeDeletionMicroserviceException
from microservice import DeletionMicroservice
from request import RemoveVectorNodeRequest
from transit import RemoveVectorNodeDispatcher
from util import LoggingLevelRouter


class VectorNodeDeletionMicroservice(DeletionMicroservice[RemoveVectorNodeRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the deletion-validation security lifecycle.

    Attributes:
        dispatcher: Optional[RemoveVectorNodeDispatcher]

    Provides:
        -   def execute(request: RemoveVectorNodeRequest) -> DeletionResult[VectorNode]

    Super Class:
        DeletionMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[RemoveVectorNodeDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[RemoveVectorNodeDispatcher]
        """
        super().__init__(dispatcher=dispatcher or RemoveVectorNodeDispatcher())
        
    @property
    def dispatcher(self) -> RemoveVectorNodeDispatcher:
        return cast(RemoveVectorNodeDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: RemoveVectorNodeRequest) -> DeletionResult[VectorNode]:
        """
        Handles RemoveVectorNodeRequests.

        Action:
            1.  Send an exception chain in the DeletionResult if the request is
                not fulfilled.
            2.  Otherwise, send the deleted VectorNode in the success result.
        Args:
            request: RemoveVectorNodeRequest
        Result:
            DeletionResult[VectorNode]
        Raises:
            VectorNodeDeletionMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            DeletionResult.failure(
                VectorNodeDeletionMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeDeletionMicroserviceException.MSG,
                    err_code=VectorNodeDeletionMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        node = cast(VectorNode, result.payload)
        return DeletionResult.success(node)