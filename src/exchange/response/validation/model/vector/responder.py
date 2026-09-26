# src/exchange/response/validation/model/vector/exchange.py

"""
Module: exchange.response.validation.model.vector.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, VectorValidationResponse
from exchange import ModelValidationResponder, VectorValidationRequest
from domain import Vector
from err import VectorValidationResponderException
from transit import VectorCarrier, VectorValidationDispatcher
from util import LoggingLevelRouter


class VectorValidationResponder(ModelValidationResponder[Vector]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Vector validation Request-Response workflow.

    Attributes:
        dispatcher: VectorValidationDispatcher[T]

    Provides:
        -   def submit(request: VectorValidationRequest[T]) -> VectorValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[VectorValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[VectorValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or VectorValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> VectorValidationDispatcher:
        return cast(VectorValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: VectorValidationRequest
    ) -> VectorValidationResponse:
        """
        Certify a candidate is a VectorCarrier whose payload is either a Vector
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: VectorValidationRequest
        Result:
            VectorValidationResponse
        Raises:
            VectorValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return VectorValidationResponse.failure(
                request=request,
                result=result,
                exception=VectorValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationResponderException.MSG,
                    err_code=VectorValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(VectorCarrier, result.payload)
        return VectorValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )