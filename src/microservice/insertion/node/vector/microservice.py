# src/microservice/insertion/node/vector/microservice.py

"""
Module: microservice.insertion.node.vector.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from typing import Optional, cast

from artifcat import InsertionResult
from domain import Vector
from err import VectorInsertionMicroserviceException
from microservice import InsertionMicroservice
from request import AddVectorNodeRequest
from transit import AddVectorNodeDispatcher
from util import LoggingLevelRouter


class VectorNodeInsertionMicroservice(InsertionMicroservice[AddVectorNodeRequest]):
    """
    Role:
        -   API
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's insertioners and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the insertion-validation security lifecycle.

    Attributes:
        dispatcher: Optional[AddVectorNodeDispatcher]

    Provides:
        -   def execute(request: AddVectorNodeRequest) -> InsertionResult

    Super Class:
        InsertionMicroservice
    """
  
    
    def __init__(
            self,
            dispatcher: Optional[AddVectorNodeDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AddVectorNodeDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AddVectorNodeDispatcher())
        
    @property
    def dispatcher(self) -> AddVectorNodeDispatcher:
        return cast(AddVectorNodeDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorNodeRequest) -> InsertionResult[Vector]:
        """
        Handles AddVectorNodeRequests.

        Action:
            1.  Send an exception chain in the InsertionResult if the request is
                not fulfilled.
            2.  Otherwise, send the success result.
        Args:
            request: AddVectorNodeRequest
        Result:
            InsertionResult
        Raises:
            VectorInsertionMicroserviceException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Dispatch the request to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that the worker does not fulfil the request.
        if result.is_failure:
            # Send an exception chain in the result.
            InsertionResult.failure(
                VectorNodeInsertionMicroserviceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeInsertionMicroserviceException.MSG,
                    err_code=VectorNodeInsertionMicroserviceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Forward the work product to the client. ---#
        return InsertionResult.success()
    
    