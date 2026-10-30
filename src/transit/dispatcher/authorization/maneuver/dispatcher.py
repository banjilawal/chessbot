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
from err import ManeuverAuthorizationDispatcherException
from exchange import ManeuverPermissionRequest, ManeuverRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter


class ManeuverAuthorizationDispatcher(AuthorizationDispatcher[ManeuverPermissionRequest]):
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
    
    def __init__(self, authorizer: Optional[ManeuverAuthorizer] | None = None):
        """
        Args:
             authorizer: Optional[ManeuverAuthorizer]
        """
        super().__init__(authorizer=authorizer or ManeuverAuthorizer())
        
    @property
    def authorizer(self) -> ManeuverAuthorizer:
        return cast(ManeuverAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverPermissionRequest) -> ManeuverDecision:
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
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request.authorization_applicant,
                exception=ManeuverAuthorizationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverAuthorizationDispatcherException.MSG,
                    err_code=ManeuverAuthorizationDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approval = decision.request
        # --- Prepare an approval from the completed chain. ---#
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)