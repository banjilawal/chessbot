# src/transit/dispatcher/encounter/kill/dispatcher.py

"""
Module: transit.dispatcher.encounter.kill.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast



class KillEncounterDispatcher(EncounterDispatcher[KillRequest]):
    """
    Role
        -   Permission Encounter Manager

    Responsibilities:
        1.  Manaage kill encounter.

    Attributes:
        authorizer: KillAuthorizer

    Provides:
        -   def  execute(request: KillRequest) -> KillDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[KillAuthorizer]):
        """
        Args:
             authorizer: Optional[KillAuthorizer]
        """
        super().__init__(authorizer=authorizer or KillAuthorizer())
        
    @property
    def authorizer(self) -> KillAuthorizer:
        return cast(KillAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: KillRequest) -> KillDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: KillRequest
        Returns:
            KillDecision
        Raises:
            KillEncounterDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return KillDecision.denial(
                request=request,
                exception=KillEncounterDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=KillEncounterDispatcherException.MSG,
                    err_code=KillEncounterDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.permission_request
        # --- Prepare an approval from the completed chain. ---#
        approval = KillRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return KillDecision.grant(approval)