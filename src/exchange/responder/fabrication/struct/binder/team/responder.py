# src/exchange/responder/fabrication/struct/binder/team/responder.py

"""
Module: exchange.responder.fabrication.struct.binder.team.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, TeamBinderBuildResponse
from domain import TeamBinder
from exchange import BinderBuildResponder, TeamBinderBuildRequest
from err import TeamBinderBuildResponderException
from transit import TeamBinderCarrier, TeamBinderBuildDispatcher
from util import LoggingLevelRouter


class TeamBinderBuildResponder(BinderBuildResponder[TeamBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the TeamBinder build Request-Response workflow.

    Attributes:
        dispatcher: TeamBinderBuildDispatcher

    Provides:
        -   def execute(request: TeamBinderBuildRequest) -> TeamBinderBuildResponse

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamBinderBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamBinderBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamBinderBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamBinderBuildDispatcher:
        return cast(TeamBinderBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamBinderBuildRequest
    ) -> TeamBinderBuildResponse:
        """
        Certify a candidate is a TeamBinderCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamBinderBuildRequest
        Result:
            TeamBinderBuildResponse
        Raises:
            TeamValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamBinderBuildResponse.failure(
                request=request,
                result=result,
                exception=TeamBinderBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderBuildResponderException.MSG,
                    err_code=TeamBinderBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamBinderCarrier, result.payload)
        return TeamBinderBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )