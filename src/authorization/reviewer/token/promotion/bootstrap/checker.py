# src/authorization/applicant/token/promotion/approver.py

"""
Module: authorization.applicant.token.promotion.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionAuthorizationLoader, ApplicantTokenReviewer
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionLoadChecker:
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:
        validation_service: TokenValidationService
        loader: Optional[PromotionAuthorizationLoader]

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        TokenApprover
    """
    _loader: PromotionAuthorizationLoader
    
    def __init__(
            self,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
        """
        self._loader = loader or PromotionAuthorizationLoader()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a Token meets the requirements to perform an activity.

        Action:
            1.  Return Promotion denial if any of the following occur:
                    -   The request is either null or the wrong type.
                    -   The applicant is not a PawnToken.
                    -   The applicant is not ready.
                    -   The applicant has already been promoted.
                    -   The actor is not on its enemy's rank row.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            TokenPromotionApproverException
        """
        method = f"{self.__class__.__name__}"
        
        load = self._loader.execute(request=request)
        if load.is_denied:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=TokenPromotionApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPromotionApproverException.MSG,
                    err_code=TokenPromotionApproverException.ERR_CODE,
                    ex=load.exception
                ),
            )
        approval = cast(PromotionRequest, load.request)
        return PromotionDecision.grant(approval)


        