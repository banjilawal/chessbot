# src/exchange/responder/authorization/model/scalar/responder.py

"""
Module: exchange.responder.authorization.model.scalar.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, ScalarDecision
from exchange import ModelAuthorizationResponder, ScalarAuthorizationRequest
from domain import Scalar
from err import ScalarAuthorizationResponderException
from transit import ScalarCarrier, ScalarAuthorizationDispatcher
from util import LoggingLevelRouter


class ScalarAuthorizationResponder(ModelAuthorizationResponder[Scalar]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Scalar authorization Request-Response workflow.

    Attributes:
        dispatcher: ScalarAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: ScalarAuthorizationRequest[T]) -> ScalarDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ScalarAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ScalarAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ScalarAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ScalarAuthorizationDispatcher:
        return cast(ScalarAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ScalarAuthorizationRequest
    ) -> ScalarDecision:
        """
        Certify a candidate is a ScalarCarrier whose payload is either a Scalar
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ScalarAuthorizationRequest
        Result:
            ScalarDecision
        Raises:
            ScalarAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ScalarDecision.failure(
                request=request,
                result=result,
                exception=ScalarAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarAuthorizationResponderException.MSG,
                    err_code=ScalarAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ScalarCarrier, result.payload)
        return ScalarDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )