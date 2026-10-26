# src/authorization/loader/promotion/loader.py

"""
Module: authorization.loader.promotion.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionDecision
from authorization import AuthorizationLoader
from err import PromotionAuthorizationLoaderException
from exchange import PromotionPermissionRequest
from util import LoggingLevelRouter


class PromotionAuthorizationLoader(AuthorizationLoader[PromotionPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Ensure only not-null PermissionRequest is processed.

    Attributes:

    Provides:
        -   def execute(request: PromotionPermissionRequest) -> PromotionDecision

    Super Class:
        AuthorizationLoader
    """
    def __init__(self):
        """Args:"""
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Checks if the request is null or the wrong type

        Action:
            1.  Send an exception chain in the Decision denial if either;
                    -   the request is null.
                    -   not a PromotionPermissionRequest.
            2.  Otherwise, send an approval.
        Args:
            request: PromotionPermissionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionAuthorizationLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request gets flagged.
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=PromotionPermissionRequest,
            null_exception=PromotionPermissionRequestNullException(),
        )
        # Send an exception chain in the denial.
        if priming.is_failure:
            return PromotionDecision.denial(
                request=request.payload,
                exception=PromotionAuthorizationLoaderException(
                   cls_mthd=method,
                   cls_name=self.__class__.__name__,
                   msg=PromotionAuthorizationLoaderException.MSG,
                   err_code=PromotionAuthorizationLoaderException.ERR_CODE,
                   ex=priming.exception,
                )
            )
        approved_request = cast(PromotionPermissionRequest, priming.payload)
        # --- Prepare an approval from the completed chain. ---#
        approval = PromotionPermissionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)