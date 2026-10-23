# src/transit/dispatcher/authorization/attack/dispatcher.py

"""
Module: transit.dispatcher.authorization.attack.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackDecision
from authorization import AttackAuthorizer
from exchange import AttackRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter


class AttackAuthorizationDispatcher(AuthorizationDispatcher[AttackRequest]):
    """
    Role
        -   Permission Authorization Manager

    Responsibilities:
        1.  Manaage attack authorization.

    Attributes:
        authorizer: AttackAuthorizer

    Provides:
        -   def  execute(request: AttackRequest) -> AttackDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[AttackAuthorizer]):
        """
        Args:
             authorizer: Optional[AttackAuthorizer]
        """
        super().__init__(authorizer=authorizer or AttackAuthorizer())
        
    @property
    def authorizer(self) -> AttackAuthorizer:
        return cast(AttackAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: AttackRequest
        Returns:
            AttackDecision
        Raises:
            AttackAuthorizationDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackAuthorizationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackAuthorizationDispatcherException.MSG,
                    err_code=AttackAuthorizationDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        # --- Prepare an approval from the completed chain. ---#
        approval = AttackRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)