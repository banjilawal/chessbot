# src/exchange/responder/authorization/struct/binder/team/responder.py

"""
Module: exchange.responder.authorization.struct.binder.team.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, TeamBinderDecision
from domain import TeamBinder
from exchange import BinderAuthorizationResponder, TeamBinderAuthorizationRequest
from err import TeamBinderAuthorizationResponderException
from transit import TeamBinderCarrier, TeamBinderAuthorizationDispatcher
from util import LoggingLevelRouter


class TeamBinderAuthorizationResponder(BinderAuthorizationResponder[TeamBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the TeamBinder authorization Request-Response workflow.

    Attributes:
        dispatcher: TeamBinderAuthorizationDispatcher

    Provides:
        -   def submit(request: TeamBinderAuthorizationRequest) -> TeamBinderDecision

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TeamBinderAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TeamBinderAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TeamBinderAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TeamBinderAuthorizationDispatcher:
        return cast(TeamBinderAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TeamBinderAuthorizationRequest
    ) -> TeamBinderDecision:
        """
        Certify a candidate is a TeamBinderCarrier whose payload is either a Team
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TeamBinderAuthorizationRequest
        Result:
            TeamBinderDecision
        Raises:
            TeamAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TeamBinderDecision.failure(
                request=request,
                result=result,
                exception=TeamBinderAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderAuthorizationResponderException.MSG,
                    err_code=TeamBinderAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TeamBinderCarrier, result.payload)
        return TeamBinderDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )