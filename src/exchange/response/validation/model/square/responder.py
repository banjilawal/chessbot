# src/exchange/response/validation/model/square/exchange.py

"""
Module: exchange.response.validation.model.square.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, SquareValidationResponse
from exchange import ModelValidationResponder, SquareValidationRequest
from domain import Square
from err import SquareValidationResponderException
from transit import SquareCarrier, SquareValidationDispatcher
from util import LoggingLevelRouter


class SquareValidationResponder(ModelValidationResponder[Square]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Square validation Request-Response workflow.

    Attributes:
        dispatcher: SquareValidationDispatcher[T]

    Provides:
        -   def submit(request: SquareValidationRequest[T]) -> SquareValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareValidationDispatcher:
        return cast(SquareValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareValidationRequest
    ) -> SquareValidationResponse:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareValidationRequest
        Result:
            SquareValidationResponse
        Raises:
            SquareValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareValidationResponse.failure(
                request=request,
                result=result,
                exception=SquareValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationResponderException.MSG,
                    err_code=SquareValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareCarrier, result.payload)
        return SquareValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )