# src/exchange/responder/validation/structure/register/square/exchange.py

"""
Module: exchange.responder.validation.structure.register.square.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, SquareRegisterValidationResponse
from domain import SquareRegister
from exchange import RegisterValidationResponder, SquareRegisterValidationRequest
from err import SquareRegisterValidationResponderException
from transit import SquareCarrier, SquareRegisterCarrier, SquareRegisterValidationDispatcher
from util import LoggingLevelRouter


class SquareRegisterValidationResponder(RegisterValidationResponder[SquareRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the SquareRegister validation Request-Response workflow.

    Attributes:
        dispatcher: SquareRegisterValidationDispatcher[T]

    Provides:
        -   def submit(request: SquareRegisterValidationRequest[T]) -> SquareRegisterValidationResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareRegisterValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareRegisterValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareRegisterValidationDispatcher:
        return cast(SquareRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareRegisterValidationRequest
    ) -> SquareRegisterValidationResponse:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            SquareRegisterValidationResponse
        Raises:
            SquareValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareRegisterValidationResponse.failure(
                request=request,
                result=result,
                exception=SquareRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationResponderException.MSG,
                    err_code=SquareRegisterValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareRegisterCarrier, result.payload)
        return SquareRegisterValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )