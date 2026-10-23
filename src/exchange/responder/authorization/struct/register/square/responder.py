# src/exchange/responder/authorization/struct/register/square/responder.py

"""
Module: exchange.responder.authorization.struct.register.square.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, SquareRegisterDecision
from domain import SquareRegister
from exchange import RegisterAuthorizationResponder, SquareRegisterAuthorizationRequest
from err import SquareRegisterAuthorizationResponderException
from transit import SquareCarrier, SquareRegisterCarrier, SquareRegisterAuthorizationDispatcher
from util import LoggingLevelRouter


class SquareRegisterAuthorizationResponder(RegisterAuthorizationResponder[SquareRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the SquareRegister authorization Request-Response workflow.

    Attributes:
        dispatcher: SquareRegisterAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: SquareRegisterAuthorizationRequest[T]) -> SquareRegisterDecision[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareRegisterAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareRegisterAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareRegisterAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareRegisterAuthorizationDispatcher:
        return cast(SquareRegisterAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareRegisterAuthorizationRequest
    ) -> SquareRegisterDecision:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareRegisterAuthorizationRequest
        Result:
            SquareRegisterDecision
        Raises:
            SquareAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareRegisterDecision.failure(
                request=request,
                result=result,
                exception=SquareRegisterAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterAuthorizationResponderException.MSG,
                    err_code=SquareRegisterAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareRegisterCarrier, result.payload)
        return SquareRegisterDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )