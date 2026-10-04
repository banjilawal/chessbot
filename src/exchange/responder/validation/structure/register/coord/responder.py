# src/exchange/responder/validation/struct/register/coord/exchange.py

"""
Module: exchange.responder.validation.struct.register.coord.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, CoordRegisterValidationResponse
from domain import CoordRegister
from exchange import RegisterValidationResponder, CoordRegisterValidationRequest
from err import CoordRegisterValidationResponderException
from transit import CoordCarrier, CoordRegisterCarrier, CoordRegisterValidationDispatcher
from util import LoggingLevelRouter


class CoordRegisterValidationResponder(RegisterValidationResponder[CoordRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the CoordRegister validation Request-Response workflow.

    Attributes:
        dispatcher: CoordRegisterValidationDispatcher[T]

    Provides:
        -   def submit(request: CoordRegisterValidationRequest[T]) -> CoordRegisterValidationResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordRegisterValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordRegisterValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordRegisterValidationDispatcher:
        return cast(CoordRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordRegisterValidationRequest
    ) -> CoordRegisterValidationResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            CoordRegisterValidationResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordRegisterValidationResponse.failure(
                request=request,
                result=result,
                exception=CoordRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationResponderException.MSG,
                    err_code=CoordRegisterValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordRegisterCarrier, result.payload)
        return CoordRegisterValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )