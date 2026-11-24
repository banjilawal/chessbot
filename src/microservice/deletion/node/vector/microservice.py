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
from request import RemoveVectorNodeRequest
from transit import RemoveVectorNodeDispatcher
from util import LoggingLevelRouter


class VectorNodeDeletionMicroservice(DeletionMicroservice[RemoveVectorNodeRequest]):
    """
    Role:
        - API
        - Lifecycle Manager
        - Operations Provider
        - Stateless Microservice
        
    About:
        Avoids casting an entity's deletioners and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the deletion-validation security lifecycle.

    Attributes:
        dispatcher: Optional[RemoveVectorNodeDispatcher]

    Provides:

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
            1.  Send an exception chain in the PushRequest if the request is
                not fulfilled.
            2.  Otherwise, send the Vector in the success result.
        Args:
            request: VectorSearchRequest
        Result:
            DeletionResult[VectorNode]
        Raises:
            VectorNodeDeletionMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        result = self.dispatcher.execute(request)
        if result.is_failure:
            DeletionResult.failure(
                VectorNodeDeletionMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeDeletionMicroserviceException.MSG,
                    err_code=VectorNodeDeletionMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        node = cast(VectorNode, result.payload)
        return DeletionResult.success(node)
    
    