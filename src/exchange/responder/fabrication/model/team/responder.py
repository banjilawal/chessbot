# src/exchange/responder/fabrication/model/team/responder.py

"""
Module: exchange.responder.fabrication.model.team.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, TeamBuildResponse
from err import TeamBuildResponderException
from exchange import ModelBuildResponder, TeamBuildRequest
from domain import Team
from transit import TeamCarrier, TeamBuildDispatcher
from util import LoggingLevelRouter


class TeamBuildResponder(ModelBuildResponder[Team]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Team build Request-Response workflow.

    Attributes:
        dispatcher: TeamBuildDispatcher[T]

    Provides:
        -   def submit(request: TeamBuildRequest[T]) -> TeamBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamBuildDispatcher:
        return cast(TeamBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamBuildRequest
    ) -> TeamBuildResponse:
        """
        Certify a candidate is a TeamCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamBuildRequest
        Result:
            TeamBuildResponse
        Raises:
            TeamValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamBuildResponse.failure(
                request=request,
                result=result,
                exception=TeamBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildResponderException.MSG,
                    err_code=TeamBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamCarrier, result.payload)
        return TeamBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )