# src/transit/dispatcher/authorization/promotion/dispatcher.py

"""
Module: transit.dispatcher.authorization.promotion.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionAuthorizer
from err import PromotionAuthorizationDispatcherException
from exchange import PromotionPermissionRequest, PromotionRequest
from transit import AuthorizationDispatcher
from util import LoggingLevelRouter


class PromotionAuthorizationDispatcher(AuthorizationDispatcher[PromotionPermissionRequest]):
    """
    Role
        -   Permission Authorization Manager

    Responsibilities:
        1.  Manaage promotion authorization.

    Attributes:
        authorizer: PromotionAuthorizer

    Provides:
        -   def  execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        Dispatcher
    """
    
    def __init__(self, authorizer: Optional[PromotionAuthorizer] | None = None):
        """
        Args:
             authorizer: Optional[PromotionAuthorizer]
        """
        super().__init__(authorizer=authorizer or PromotionAuthorizer())
        
    @property
    def authorizer(self) -> PromotionAuthorizer:
        return cast(PromotionAuthorizer, super().authorizer)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Decide if a Token can be promoted.
        
        Action:
            1.  Send
        Args:
            request: PromotionRequest
        Returns:
            PromotionDecision
        Raises:
            PromotionAuthorizationDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the authorizer does not grant permission.
        decision = self.authorizer.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request.payload,
                exception=PromotionAuthorizationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionAuthorizationDispatcherException.MSG,
                    err_code=PromotionAuthorizationDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approval = decision.request
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)