# src/exchange/responder/validation/struct/chart/footstep/responder.py

"""
Module: exchange.responder.validation.struct.chart.footstep.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Footstep
from exchange import ChartValidationResponder
from util import LoggingLevelRouter


class FootstepValidationResponder(ChartValidationResponder[Footstep]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Footstep validation Request-Response workflow.

    Attributes:
        dispatcher: FootstepValidationDispatcher[T]

    Provides:
        -   def submit(request: FootstepValidationRequest[T]) -> FootstepValidationResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[FootstepValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[FootstepValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or FootstepValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> FootstepValidationDispatcher:
        return cast(FootstepValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepValidationRequest
    ) -> FootstepValidationResponse:
        """
        Certify a candidate is a CoordCarrier whose payload is either a Coord
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: FootstepValidationRequest
        Result:
            FootstepValidationResponse
        Raises:
            CoordValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return FootstepValidationResponse.failure(
                request=request,
                result=result,
                exception=FootstepValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationResponderException.MSG,
                    err_code=FootstepValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(FootstepCarrier, result.payload)
        return FootstepValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )