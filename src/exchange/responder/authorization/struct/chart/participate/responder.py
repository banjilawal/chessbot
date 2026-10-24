# src/exchange/responder/authorization/struct/chart/participate/responder.py

"""
Module: exchange.responder.authorization.struct.chart.participate.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, ParticipationDecision
from domain import Participation
from exchange import ChartAuthorizationResponder, FootstepAuthorizationRequest
from err import ParticipationAuthorizationResponderException
from transit import TokenCarrier, ParticipationCarrier, ParticipationAuthorizationDispatcher
from util import LoggingLevelRouter


class ParticipationAuthorizationResponder(ChartAuthorizationResponder[Participation]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Participation authorization Request-Response workflow.

    Attributes:
        dispatcher: ParticipationAuthorizationDispatcher[T]

    Provides:
        -   def execute(request: ParticipationAuthorizationRequest[T]) -> ParticipationDecision[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ParticipationAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ParticipationAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ParticipationAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ParticipationAuthorizationDispatcher:
        return cast(ParticipationAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepAuthorizationRequest
    ) -> ParticipationDecision:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ParticipationAuthorizationRequest
        Result:
            ParticipationDecision
        Raises:
            TokenAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ParticipationDecision.failure(
                request=request,
                result=result,
                exception=ParticipationAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationAuthorizationResponderException.MSG,
                    err_code=ParticipationAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ParticipationCarrier, result.payload)
        return ParticipationDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )