# src/exchange/responder/validation/model/scalar/exchange.py

"""
Module: exchange.responder.validation.model.scalar.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, ScalarValidationResponse
from exchange import ModelValidationResponder, ScalarValidationRequest
from domain import Scalar
from err import ScalarValidationResponderException
from transit import ScalarCarrier, ScalarValidationDispatcher
from util import LoggingLevelRouter


class ScalarValidationResponder(ModelValidationResponder[Scalar]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Scalar validation Request-Response workflow.

    Attributes:
        dispatcher: ScalarValidationDispatcher[T]

    Provides:
        -   def submit(request: ScalarValidationRequest[T]) -> ScalarValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ScalarValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ScalarValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ScalarValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ScalarValidationDispatcher:
        return cast(ScalarValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ScalarValidationRequest
    ) -> ScalarValidationResponse:
        """
        Certify a candidate is a ScalarCarrier whose payload is either a Scalar
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ScalarValidationRequest
        Result:
            ScalarValidationResponse
        Raises:
            ScalarValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ScalarValidationResponse.failure(
                request=request,
                result=result,
                exception=ScalarValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationResponderException.MSG,
                    err_code=ScalarValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ScalarCarrier, result.payload)
        return ScalarValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )