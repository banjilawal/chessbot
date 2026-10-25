# src/transit/dispatcher/encounter/warning/dispatcher.py

"""
Module: transit.dispatcher.encounter.warning.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import WarningDecision
from encounter import WarningAuthorizer
from err import WarningEncounterDispatcherException
from exchange import WarningRequest
from transit import EncounterDispatcher
from util import LoggingLevelRouter


class EncounterWarningDispatcher(EncounterDispatcher[WarningRequest]):
    """
    Role
        -   Permission Encounter Manager

    Responsibilities:
        1.  Manaage warning encounter.

    Attributes:
        authorizer: WarningAuthorizer

    Provides:
        -   def  execute(request: WarningRequest) -> WarningDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[WarningAuthorizer]):
        """
        Args:
             authorizer: Optional[WarningAuthorizer]
        """
        super().__init__(authorizer=authorizer or WarningAuthorizer())
        
    @property
    def authorizer(self) -> WarningAuthorizer:
        return cast(WarningAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: WarningRequest) -> WarningDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: WarningRequest
        Returns:
            WarningDecision
        Raises:
            WarningEncounterDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return WarningDecision.denial(
                request=request,
                exception=WarningEncounterDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningEncounterDispatcherException.MSG,
                    err_code=WarningEncounterDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.permission_request
        # --- Prepare an approval from the completed chain. ---#
        approval = WarningRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return WarningDecision.grant(approval)