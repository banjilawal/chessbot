# src/exchange/responder/fabrication/model/alert/responder.py

"""
Module: exchange.responder.fabrication.model.alert.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, AlertBuildResponse
from exchange import ModelBuildResponder, AlertBuildRequest
from domain import Alert
from err import AlertBuildResponderException
from transit import AlertCarrier, AlertBuildDispatcher
from util import LoggingLevelRouter


class AlertBuildResponder(ModelBuildResponder[Alert]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Alert build Request-Response workflow.

    Attributes:
        dispatcher: AlertBuildDispatcher[T]

    Provides:
        -   def execute(request: AlertBuildRequest[T]) -> AlertBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AlertBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AlertBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AlertBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> AlertBuildDispatcher:
        return cast(AlertBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AlertBuildRequest
    ) -> AlertBuildResponse:
        """
        Certify a candidate is a AlertCarrier whose payload is either a Alert
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AlertBuildRequest
        Result:
            AlertBuildResponse
        Raises:
            AlertValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AlertBuildResponse.failure(
                request=request,
                result=result,
                exception=AlertBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertBuildResponderException.MSG,
                    err_code=AlertBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AlertCarrier, result.authorization_applicant)
        return AlertBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )