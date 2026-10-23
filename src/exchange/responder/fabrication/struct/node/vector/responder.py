# src/exchange/responder/fabrication/struct/node/vector/responder.py

"""
Module: exchange.responder.fabrication.struct.node.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, VectorNodeBuildResponse
from domain import VectorNode
from exchange import NodeBuildResponder, VectorNodeBuildRequest
from err import VectorNodeBuildResponderException
from transit import VectorCarrier, VectorNodeCarrier, VectorNodeBuildDispatcher
from util import LoggingLevelRouter


class VectorNodeBuildResponder(NodeBuildResponder[VectorNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorNode build Request-Response workflow.

    Attributes:
        dispatcher: VectorNodeBuildDispatcher[T]

    Provides:
        -   def submit(request: VectorNodeBuildRequest[T]) -> VectorNodeBuildResponse[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorNodeBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorNodeBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorNodeBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorNodeBuildDispatcher:
        return cast(VectorNodeBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorNodeBuildRequest
    ) -> VectorNodeBuildResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorNodeBuildRequest
        Result:
            VectorNodeBuildResponse
        Raises:
            VectorValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorNodeBuildResponse.failure(
                request=request,
                result=result,
                exception=VectorNodeBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeBuildResponderException.MSG,
                    err_code=VectorNodeBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorNodeCarrier, result.payload)
        return VectorNodeBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )