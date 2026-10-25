# src/exchange/responder/authorization/attack/responder.py

"""
Module: exchange.responder.authorization.attack.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackDecision
from err import AttackAuthorizationResponderException
from exchange import AuthorizationResponder, AttackPermissionRequest, EncounterRequest
from transit import AttackAuthorizationDispatcher
from util import LoggingLevelRouter


class AttackAuthorizationResponder(
    AuthorizationResponder[AttackDecision]
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Attack authorization Request-Response workflow.

    Attributes:
        dispatcher: AttackAuthorizationDispatcher

    Provides:
        -   def execute(request: AttackPermissionRequest) -> AttackDecision

    Super Class:
        AuthorizationResponder
    """
    
    def __init__(self, dispatcher: Optional[AttackAuthorizationDispatcher] | None = None,):
        """
        Args:
            dispatcher: Optional[AttackAuthorizationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or AttackAuthorizationDispatcher())
        
    @property
    def dispatcher(self) -> AttackAuthorizationDispatcher:
        return cast(AttackAuthorizationDispatcher, super().dispatcher)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackPermissionRequest) -> AttackDecision:
        """
        Args:
            request: AttackPermissionRequest
        Result:
            AttackDecision
        Raises:
            AttackAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.dispatcher.execute(request)
        if decision.request_is_denied:
            return AttackDecision.denial(
                request=request.candidate,
                exception=AttackAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackAuthorizationResponderException.MSG,
                    err_code=AttackAuthorizationResponderException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approval = cast(AttackRequest, decision.candidate)
        return AttackDecision.grant(approval)
        
        