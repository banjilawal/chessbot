# src/exchange/responder/authorization/struct/node/vector/responder.py

"""
Module: exchange.responder.authorization.struct.node.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, VectorNodeDecision
from domain import VectorNode
from exchange import NodeAuthorizationResponder, VectorNodePermissionRequest
from err import VectorNodeAuthorizationResponderException
from transit import VectorCarrier, VectorNodeCarrier, VectorNodeAuthorizationDispatcher
from util import LoggingLevelRouter


class VectorNodeAuthorizationResponder(NodeAuthorizationResponder[VectorNode]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorNode authorization Request-Response workflow.

    Attributes:
        dispatcher: VectorNodeAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: VectorNodePermissionRequest[T]) -> VectorNodeDecision[T]

    Super Class:
        NodeValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorNodeAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorNodeAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorNodeAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorNodeAuthorizationDispatcher:
        return cast(VectorNodeAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorNodePermissionRequest
    ) -> VectorNodeDecision:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorNodePermissionRequest
        Result:
            VectorNodeDecision
        Raises:
            VectorAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorNodeDecision.failure(
                request=request,
                result=result,
                exception=VectorNodeAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeAuthorizationResponderException.MSG,
                    err_code=VectorNodeAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorNodeCarrier, result.payload)
        return VectorNodeDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )