# src/exchange/responder/fabrication/struct/chart/participate/responder.py

"""
Module: exchange.responder.fabrication.struct.chart.participate.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ParticipationBuildResponse
from domain import Participation
from exchange import ChartBuildResponder, FootstepBuildRequest
from err import ParticipationBuildResponderException
from transit import TokenCarrier, ParticipationCarrier, ParticipationBuildDispatcher
from util import LoggingLevelRouter


class ParticipationBuildResponder(ChartBuildResponder[Participation]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Participation build Request-Response workflow.

    Attributes:
        dispatcher: ParticipationBuildDispatcher[T]

    Provides:
        -   def execute(request: ParticipationBuildRequest[T]) -> ParticipationBuildResponse[T]

    Super Class:
        ChartValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ParticipationBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ParticipationBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ParticipationBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> ParticipationBuildDispatcher:
        return cast(ParticipationBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: FootstepBuildRequest
    ) -> ParticipationBuildResponse:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ParticipationBuildRequest
        Result:
            ParticipationBuildResponse
        Raises:
            TokenValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ParticipationBuildResponse.failure(
                request=request,
                result=result,
                exception=ParticipationBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationBuildResponderException.MSG,
                    err_code=ParticipationBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ParticipationCarrier, result.authorization_applicant)
        return ParticipationBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )