# src/exchange/responder/validation/model/alert/responder.py

"""
Module: exchange.responder.validation.model.alert.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, AlertValidationResponse
from exchange import ModelValidationResponder, AlertValidationRequest
from domain import Alert
from err import AlertValidationResponderException
from transit import AlertCarrier, AlertValidationDispatcher
from util import LoggingLevelRouter


class AlertValidationResponder(ModelValidationResponder[Alert]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Alert validation Request-Response workflow.

    Attributes:
        dispatcher: AlertValidationDispatcher[T]

    Provides:
        -   def submit(request: AlertValidationRequest[T]) -> AlertValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AlertValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AlertValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AlertValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AlertValidationDispatcher:
        return cast(AlertValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AlertValidationRequest
    ) -> AlertValidationResponse:
        """
        Certify a candidate is a AlertCarrier whose payload is either a Alert
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AlertValidationRequest
        Result:
            AlertValidationResponse
        Raises:
            AlertValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AlertValidationResponse.failure(
                request=request,
                result=result,
                exception=AlertValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationResponderException.MSG,
                    err_code=AlertValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AlertCarrier, result.payload)
        return AlertValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )