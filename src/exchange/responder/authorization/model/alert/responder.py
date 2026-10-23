# src/exchange/responder/authorization/model/alert/responder.py

"""
Module: exchange.responder.authorization.model.alert.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, AlertDecision
from exchange import ModelAuthorizationResponder, AlertAuthorizationRequest
from domain import Alert
from err import AlertAuthorizationResponderException
from transit import AlertCarrier, AlertAuthorizationDispatcher
from util import LoggingLevelRouter


class AlertAuthorizationResponder(ModelAuthorizationResponder[Alert]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Alert authorization Request-Response workflow.

    Attributes:
        dispatcher: AlertAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: AlertAuthorizationRequest[T]) -> AlertDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AlertAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AlertAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AlertAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AlertAuthorizationDispatcher:
        return cast(AlertAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AlertAuthorizationRequest
    ) -> AlertDecision:
        """
        Certify a candidate is a AlertCarrier whose payload is either a Alert
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AlertAuthorizationRequest
        Result:
            AlertDecision
        Raises:
            AlertAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AlertDecision.failure(
                request=request,
                result=result,
                exception=AlertAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertAuthorizationResponderException.MSG,
                    err_code=AlertAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AlertCarrier, result.payload)
        return AlertDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )