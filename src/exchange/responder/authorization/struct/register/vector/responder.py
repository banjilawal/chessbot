# src/exchange/responder/authorization/struct/register/vector/responder.py

"""
Module: exchange.responder.authorization.struct.register.vector.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, VectorRegisterDecision
from domain import VectorRegister
from exchange import RegisterAuthorizationResponder, VectorRegisterAuthorizationRequest
from err import VectorRegisterAuthorizationResponderException
from transit import VectorCarrier, VectorRegisterCarrier, VectorRegisterAuthorizationDispatcher
from util import LoggingLevelRouter


class VectorRegisterAuthorizationResponder(RegisterAuthorizationResponder[VectorRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorRegister authorization Request-Response workflow.

    Attributes:
        dispatcher: VectorRegisterAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: VectorRegisterAuthorizationRequest[T]) -> VectorRegisterDecision[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorRegisterAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorRegisterAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorRegisterAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorRegisterAuthorizationDispatcher:
        return cast(VectorRegisterAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorRegisterAuthorizationRequest
    ) -> VectorRegisterDecision:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorRegisterAuthorizationRequest
        Result:
            VectorRegisterDecision
        Raises:
            VectorAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorRegisterDecision.failure(
                request=request,
                result=result,
                exception=VectorRegisterAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterAuthorizationResponderException.MSG,
                    err_code=VectorRegisterAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorRegisterCarrier, result.payload)
        return VectorRegisterDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )