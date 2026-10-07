# src/exchange/responder/validation/struct/chart/participate/responder.py

"""
Module: exchange.responder.validation.struct.chart.participate.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, ParticipationValidationResponse
from domain import Participation
from exchange import ChartValidationResponder, FootstepValidationRequest
from err import ParticipationValidationResponderException
from transit import TokenCarrier, ParticipationCarrier, ParticipationValidationDispatcher
from util import LoggingLevelRouter


class ParticipationValidationResponder(ChartValidationResponder[Participation]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Participation validation Request-Response workflow.

    Attributes:
        dispatcher: ParticipationValidationDispatcher[T]

    Provides:
        -   def submit(request: ParticipationValidationRequest[T]) -> ParticipationValidationResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ParticipationValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ParticipationValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ParticipationValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ParticipationValidationDispatcher:
        return cast(ParticipationValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepValidationRequest
    ) -> ParticipationValidationResponse:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ParticipationValidationRequest
        Result:
            ParticipationValidationResponse
        Raises:
            TokenValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ParticipationValidationResponse.failure(
                request=request,
                result=result,
                exception=ParticipationValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationResponderException.MSG,
                    err_code=ParticipationValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ParticipationCarrier, result.payload)
        return ParticipationValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )