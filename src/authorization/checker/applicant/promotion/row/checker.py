# src/authorization/checker/applicant/promotion/row/checker.py

"""
Module: authorization.checker.applicant.promotion.row.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from artifcat import PromotionDecision
from authorization import PromotionTokenChecker
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionRowChecker(PromotionTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Promotion applicant is on its enemy's rank row.

    Attributes:

    Provides:
        -   def execute(self, request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionTokenChecker
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
        
        promotion_row = request.applicant.team.enemy_rank_row
        current_row = request.applicant.footstep.position.row
        
        if current_row is None or current_row != promotion_row:
            return PromotionDecision.denial(
                request=request,
                exception=PromotionRowException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRowException.MSG,
                    err_code=PromotionRowException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---
        approval = PromotionRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        return PromotionDecision.grant(approval)
 