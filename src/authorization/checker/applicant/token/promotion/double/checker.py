# src/authorization/checker/applicant/token/promotion/double/checker.py

"""
Module: authorization.checker.applicant.token.promotion.double.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from artifcat import PromotionDecision
from authorization import PromotionApplicantChecker
from exchange import PromotionRequest
from util import LoggingLevelRouter


class DoublePromotionChecker(PromotionApplicantChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Promotion applicant is on its enemy's rank double.

    Attributes:

    Provides:
        -   def execute(self, request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionApplicantChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a Token meets the requirements to perform an activity.

        Args:
            request: request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            TypeError
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        if request.applicant.is_promoted:
            return PromotionDecision.denial(
                request=request,
                exception=DoublePromotionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DoublePromotionException.MSG,
                    err_code=DoublePromotionException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---
        approval = PromotionRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        return PromotionDecision.grant(approval)
 