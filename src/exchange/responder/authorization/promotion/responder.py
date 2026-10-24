# src/exchange/responder/authorization/promotion/responder.py

"""
Module: exchange.responder.authorization.promotion.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from err import PromotionAuthorizationResponderException
from exchange import AuthorizationResponder, PromotionAuthorizationRequest, PromotionRequest
from transit import PromotionAuthorizationDispatcher
from util import LoggingLevelRouter


class PromotionAuthorizationResponder(
    AuthorizationResponder[PromotionRequest]
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Promotion authorization Request-Response workflow.

    Attributes:
        dispatcher: PromotionAuthorizationDispatcher

    Provides:
        -   def execute(request: PromotionAuthorizationRequest) -> PromotionDecision

    Super Class:
        AuthorizationResponder
    """
    
    def __init__(self, dispatcher: Optional[PromotionAuthorizationDispatcher] | None = None,):
        """
        Args:
            dispatcher: Optional[PromotionAuthorizationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or PromotionAuthorizationDispatcher())
        
    @property
    def dispatcher(self) -> PromotionAuthorizationDispatcher:
        return cast(PromotionAuthorizationDispatcher, super().dispatcher)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionAuthorizationRequest) -> PromotionDecision:
        """
        Args:
            request: PromotionAuthorizationRequest
        Result:
            PromotionDecision
        Raises:
            PromotionAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.dispatcher.execute(request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request.candidate,
                exception=PromotionAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationResponderException.MSG,
                    err_code=PromotionAuthorizationResponderException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approval = cast(PromotionRequest, decision.candidate)
        return PromotionDecision.grant(approval)
        
        