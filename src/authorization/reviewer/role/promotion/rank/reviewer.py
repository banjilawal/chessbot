# src/authorization/reviewer/role/promotion/rank/reviewer.py

"""
Module: authorization.reviewer.role.promotion.rank.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionDecision
from authorization import PromotionRoleReviewer
from domain import Elevateable
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionRankReviewer(PromotionRoleReviewer[Elevateable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        checker: PromotionRankChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionRoleReviewer
    """

    def __init__(self):
        super().__init__()
       
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self.checker.execute(request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=PromotionRankReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRankReviewerException.MSG,
                    err_code=PromotionRankReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        grant = decision.request
        approval = PromotionRequest(
            id=grant.id,
            activity=grant.activity,
            applicant=grant.applicant,
        )
        return PromotionDecision.grant(approval)
        