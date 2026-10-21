# src/authorization/activity/rank/promotion/row/checker.py

"""
Module: authorization.activity.rank.promotion.row.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import PromotionDecision
from authorization import Checker
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionRowChecker(Checker[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Rank can be promoted.

    Attributes:

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        Checker
    """
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Deny the request if requestor is not on their promotion row. Otherwise
        forward an approval.
        
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
           PromotionRowException
        """
        method = f"{self.__class__.__name__}.execute"
        
        promotion_row = request.activity.team.enemy_rank_row
        position = request.activity.footstep.position
        
        if position is None or position.row != promotion_row:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionRowException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRowException.MSG,
                    err_code=PromotionRowException.ERR_CODE,
                )
            )
        approval = PromotionRequest(
            id=request.id,
            activity=request.activity,
            activity=request.activity,
        )
        return PromotionDecision.grant(approval)
        