# src/transit/dispatcher/authorization/promotion/dispatcher.py

"""
Module: transit.dispatcher.authorization.promotion.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionPermitter
from err import PromotionPermissionDispatcherException
from exchange import PromotionPermissionRequest, PromotionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter


class PromotionPermissionDispatcher(
    PermissionDispatcher[PromotionPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a PromotionPermitter then send the results
            back to clients.

    Attributes:
        permitter: PromotionPermitter

    Provides:
        -   def  execute(candidate: Any) -> PromotionDecision

    Super Class:
        PermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[PromotionPermitter] | None = None):
        """
        Args:
             permitter: Optional[PromotionPermitter]
        """
        super().__init__(permitter=permitter or PromotionPermitter())
        
    @property
    def permitter(self) -> PromotionPermitter:
        return cast(PromotionPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> PromotionDecision:
        """
        Make a decision about a PromotionRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the PromotionRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            PromotionDecision
        Raises:
            PromotionPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                exception=PromotionPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPermissionDispatcherException.MSG,
                    err_code=PromotionPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(PromotionPermissionRequest, decision.permission_request)
        transaction_request = cast(PromotionRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return PromotionDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )