# src/exchange/responder/authorization/model/vector/responder.py

"""
Module: exchange.responder.authorization.model.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, VectorDecision
from exchange import ModelAuthorizationResponder, VectorAuthorizationRequest
from domain import Vector
from err import VectorAuthorizationResponderException
from transit import VectorCarrier, VectorAuthorizationDispatcher
from util import LoggingLevelRouter


class VectorAuthorizationResponder(ModelAuthorizationResponder[Vector]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Vector authorization Request-Response workflow.

    Attributes:
        dispatcher: VectorAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: VectorAuthorizationRequest[T]) -> VectorDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorAuthorizationDispatcher:
        return cast(VectorAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorAuthorizationRequest
    ) -> VectorDecision:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorAuthorizationRequest
        Result:
            VectorDecision
        Raises:
            VectorAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorDecision.failure(
                request=request,
                result=result,
                exception=VectorAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAuthorizationResponderException.MSG,
                    err_code=VectorAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorCarrier, result.payload)
        return VectorDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )