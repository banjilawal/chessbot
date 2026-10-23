# src/transit/dispatcher/authorization/maneuver/dispatcher.py

"""
Module: transit.dispatcher.authorization.maneuver.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverDecision
from authorization import ManeuverAuthorizer
from exchange import ManeuverRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter


class ManeuverAuthorizationDispatcher(AuthorizationDispatcher[ManeuverRequest]):
    """
    Role
        -   Permission Authorization Manager

    Responsibilities:
        1.  Manaage maneuver authorization.

    Attributes:
        authorizer: ManeuverAuthorizer

    Provides:
        -   def  execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[ManeuverAuthorizer]):
        """
        Args:
             authorizer: Optional[ManeuverAuthorizer]
        """
        super().__init__(authorizer=authorizer or ManeuverAuthorizer())
        
    @property
    def authorizer(self) -> ManeuverAuthorizer:
        return cast(ManeuverAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: ManeuverRequest
        Returns:
            ManeuverDecision
        Raises:
            ManeuverAuthorizationDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverAuthorizationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationDispatcherException.MSG,
                    err_code=ManeuverAuthorizationDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        # --- Prepare an approval from the completed chain. ---#
        approval = ManeuverRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)