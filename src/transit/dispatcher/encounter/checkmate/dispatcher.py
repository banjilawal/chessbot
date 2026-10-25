# src/transit/dispatcher/encounter/checkmate/dispatcher.py

"""
Module: transit.dispatcher.encounter.checkmate.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CheckmateDecision
from encounter import CheckmateAuthorizer
from err import CheckmateEncounterDispatcherException
from exchange import CheckmateRequest
from transit import EncounterDispatcher
from util import LoggingLevelRouter


class CheckmateEncounterDispatcher(EncounterDispatcher[CheckmateRequest]):
    """
    Role
        -   Permission Encounter Manager

    Responsibilities:
        1.  Manaage checkmate encounter.

    Attributes:
        authorizer: CheckmateAuthorizer

    Provides:
        -   def  execute(request: CheckmateRequest) -> CheckmateDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[CheckmateAuthorizer]):
        """
        Args:
             authorizer: Optional[CheckmateAuthorizer]
        """
        super().__init__(authorizer=authorizer or CheckmateAuthorizer())
        
    @property
    def authorizer(self) -> CheckmateAuthorizer:
        return cast(CheckmateAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: CheckmateRequest) -> CheckmateDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: CheckmateRequest
        Returns:
            CheckmateDecision
        Raises:
            CheckmateEncounterDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return CheckmateDecision.denial(
                request=request,
                exception=CheckmateEncounterDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CheckmateEncounterDispatcherException.MSG,
                    err_code=CheckmateEncounterDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.permission_request
        # --- Prepare an approval from the completed chain. ---#
        approval = CheckmateRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return CheckmateDecision.grant(approval)