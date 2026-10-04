# src/exchange/responder/validation/structure/register/vector/exchange.py

"""
Module: exchange.responder.validation.structure.register.vector.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, VectorRegisterValidationResponse
from domain import VectorRegister
from exchange import RegisterValidationResponder, VectorRegisterValidationRequest
from err import VectorRegisterValidationResponderException
from transit import VectorCarrier, VectorRegisterCarrier, VectorRegisterValidationDispatcher
from util import LoggingLevelRouter


class VectorRegisterValidationResponder(RegisterValidationResponder[VectorRegister]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the VectorRegister validation Request-Response workflow.

    Attributes:
        dispatcher: VectorRegisterValidationDispatcher[T]

    Provides:
        -   def submit(request: VectorRegisterValidationRequest[T]) -> VectorRegisterValidationResponse[T]

    Super Class:
        RegisterValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorRegisterValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorRegisterValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorRegisterValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorRegisterValidationDispatcher:
        return cast(VectorRegisterValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorRegisterValidationRequest
    ) -> VectorRegisterValidationResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            VectorRegisterValidationResponse
        Raises:
            VectorValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorRegisterValidationResponse.failure(
                request=request,
                result=result,
                exception=VectorRegisterValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationResponderException.MSG,
                    err_code=VectorRegisterValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorRegisterCarrier, result.payload)
        return VectorRegisterValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )