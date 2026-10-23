# src/exchange/responder/authorization/model/team/responder.py

"""
Module: exchange.responder.authorization.model.team.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, TeamDecision
from err import TeamAuthorizationResponderException
from exchange import ModelAuthorizationResponder, TeamAuthorizationRequest
from domain import Team
from transit import TeamCarrier, TeamAuthorizationDispatcher
from util import LoggingLevelRouter


class TeamAuthorizationResponder(ModelAuthorizationResponder[Team]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Team authorization Request-Response workflow.

    Attributes:
        dispatcher: TeamAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: TeamAuthorizationRequest[T]) -> TeamDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamAuthorizationDispatcher:
        return cast(TeamAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamAuthorizationRequest
    ) -> TeamDecision:
        """
        Certify a candidate is a TeamCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamAuthorizationRequest
        Result:
            TeamDecision
        Raises:
            TeamAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamDecision.failure(
                request=request,
                result=result,
                exception=TeamAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamAuthorizationResponderException.MSG,
                    err_code=TeamAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamCarrier, result.payload)
        return TeamDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )