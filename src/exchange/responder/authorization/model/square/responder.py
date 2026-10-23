# src/exchange/responder/authorization/model/square/responder.py

"""
Module: exchange.responder.authorization.model.square.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, SquareDecision
from exchange import ModelAuthorizationResponder, SquareAuthorizationRequest
from domain import Square
from err import SquareAuthorizationResponderException
from transit import SquareCarrier, SquareAuthorizationDispatcher
from util import LoggingLevelRouter


class SquareAuthorizationResponder(ModelAuthorizationResponder[Square]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Square authorization Request-Response workflow.

    Attributes:
        dispatcher: SquareAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: SquareAuthorizationRequest[T]) -> SquareDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareAuthorizationDispatcher:
        return cast(SquareAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareAuthorizationRequest
    ) -> SquareDecision:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareAuthorizationRequest
        Result:
            SquareDecision
        Raises:
            SquareAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareDecision.failure(
                request=request,
                result=result,
                exception=SquareAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareAuthorizationResponderException.MSG,
                    err_code=SquareAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareCarrier, result.payload)
        return SquareDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )