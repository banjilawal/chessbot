# src/exchange/responder/validation/struct/chart/coord/exchange.py

"""
Module: exchange.responder.validation.struct.chart.coord.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, CoordChartValidationResponse
from domain import CoordChart
from exchange import ChartValidationResponder, CoordChartValidationRequest
from err import CoordChartValidationResponderException
from transit import CoordCarrier, CoordChartCarrier, CoordChartValidationDispatcher
from util import LoggingLevelRouter


class CoordChartValidationResponder(ChartValidationResponder[CoordChart]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the CoordChart validation Request-Response workflow.

    Attributes:
        dispatcher: CoordChartValidationDispatcher[T]

    Provides:
        -   def submit(request: CoordChartValidationRequest[T]) -> CoordChartValidationResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[CoordChartValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordChartValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or CoordChartValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> CoordChartValidationDispatcher:
        return cast(CoordChartValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: CoordChartValidationRequest
    ) -> CoordChartValidationResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: CoordChartValidationRequest
        Result:
            CoordChartValidationResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return CoordChartValidationResponse.failure(
                request=request,
                result=result,
                exception=CoordChartValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationResponderException.MSG,
                    err_code=CoordChartValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(CoordChartCarrier, result.payload)
        return CoordChartValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )