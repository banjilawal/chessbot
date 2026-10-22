# src/authorization/reviewer/promotion/activity/reviewer.py

"""
Module: authorization.reviewer.promotion.activity.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import PromotionDecision
from authorization import RoleReviewer, ValidElevationChecker
from domain import Elevatable
from exchange import PromotionRequest

from util import LoggingLevelRouter


class PromotionRoleReviewer(RoleReviewer[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_item_checker: ValidRankChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        RPromotionReviewer
    """

    
    def __init__(
            self,
            valid_item_checker: Optional[ValidElevationChecker] | None = None,
    ):
        """
        Args:
            valid_item_checker: Optional[ValidRankChecker]
        """
        super().__init__(valid_item_checker=valid_item_checker or ValidElevationChecker())
        
    @property
    def valid_item_checker(self) -> ValidElevationChecker:
        return cast(ValidElevationChecker, super().valid_item_checker)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        method = f"{self.__class__.__name__}.execute"
        
        
        decision = self.valid_item_checker.execute(request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ActivityApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ActivityApproverException.MSG,
                    err_code=ActivityApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        activity = cast(Elevatable, decision.request.activity)
        approval = PromotionRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        return PromotionDecision.grant(approval)
        