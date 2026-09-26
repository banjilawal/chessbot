# src/exchange/validation/model/token/exchange.py

"""
Module: exchange.validation.model.token.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, TokenValidationResponse
from exchange import ModelValidationResponseService, TokenValidationRequest
from domain import Token
from err import TokenValidatorResponseServiceException
from transit import TokenCarrier, TokenValidationDispatcher
from util import LoggingLevelRouter


class TokenValidationResponseService(ModelValidationResponseService[Token]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Token validation Request-Response workflow.

    Attributes:
        dispatcher: TokenValidationDispatcher[T]

    Provides:
        -   def submit(request: TokenValidationRequest[T]) -> TokenValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TokenValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TokenValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TokenValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TokenValidationDispatcher:
        return cast(TokenValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenValidationRequest
    ) -> TokenValidationResponse:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TokenValidationRequest
        Result:
            TokenValidationResponse
        Raises:
            TokenValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TokenValidationResponse.failure(
                request=request,
                result=result,
                exception=TokenValidatorResponseServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorResponseServiceException.MSG,
                    err_code=TokenValidatorResponseServiceException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TokenCarrier, result.payload)
        return TokenValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )