# src/exchange/responder/validation/struct/chart/participate/exchange.py

"""
Module: exchange.responder.validation.struct.chart.participate.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, TokenChartValidationResponse
from domain import Participation
from exchange import ChartValidationResponder, TokenChartValidationRequest
from err import TokenChartValidationResponderException
from transit import TokenCarrier, TokenChartCarrier, TokenChartValidationDispatcher
from util import LoggingLevelRouter


class TokenChartValidationResponder(ChartValidationResponder[Participation]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the TokenChart validation Request-Response workflow.

    Attributes:
        dispatcher: TokenChartValidationDispatcher[T]

    Provides:
        -   def submit(request: TokenChartValidationRequest[T]) -> TokenChartValidationResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TokenChartValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TokenChartValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TokenChartValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TokenChartValidationDispatcher:
        return cast(TokenChartValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenChartValidationRequest
    ) -> TokenChartValidationResponse:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TokenChartValidationRequest
        Result:
            TokenChartValidationResponse
        Raises:
            TokenValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TokenChartValidationResponse.failure(
                request=request,
                result=result,
                exception=TokenChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationResponderException.MSG,
                    err_code=TokenChartValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TokenChartCarrier, result.payload)
        return TokenChartValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )