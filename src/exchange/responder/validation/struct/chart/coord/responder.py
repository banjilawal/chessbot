# src/exchange/responder/validation/struct/chart/walk/exchange.py

"""
Module: exchange.responder.validation.struct.chart.walk.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, WalkValidationResponse
from domain import Walk
from exchange import ChartValidationResponder, WalkValidationRequest
from err import WalkValidationResponderException
from transit import CoordCarrier, WalkCarrier, WalkValidationDispatcher
from util import LoggingLevelRouter


class WalkValidationResponder(ChartValidationResponder[Walk]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Walk validation Request-Response workflow.

    Attributes:
        dispatcher: WalkValidationDispatcher[T]

    Provides:
        -   def submit(request: WalkValidationRequest[T]) -> WalkValidationResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[WalkValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[WalkValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or WalkValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> WalkValidationDispatcher:
        return cast(WalkValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: WalkValidationRequest
    ) -> WalkValidationResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: WalkValidationRequest
        Result:
            WalkValidationResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return WalkValidationResponse.failure(
                request=request,
                result=result,
                exception=WalkValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationResponderException.MSG,
                    err_code=WalkValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(WalkCarrier, result.payload)
        return WalkValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )