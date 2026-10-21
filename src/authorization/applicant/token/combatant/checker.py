# src/authorization/applicant/token/approver.py

"""
Module: authorization.applicant.token.promotion.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import PromotionDecision
from authorization import Checker
from err import DisabledTokenException
from exchange import PromotionRequest
from util import LoggingLevelRouter


class DisabledCombatantTokenChecker(Checker[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        Checker
    """
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Deny the request if requestor has already been promoted. Otherwise,
        forward an approval.
        
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            DisabledTokenException
        """
        method = f"{self.__class__.__name__}.execute"

        if request.applicant.is_not_ready:
            # Send an exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=DisabledTokenException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DisabledTokenException.MSG,
                    err_code=DisabledTokenException.ERR_CODE,
                ),
            )
        approval = PromotionRequest(
            id=request.id,
            activity=request.activity,
            applicant=request.applicant,
        )
        return PromotionDecision.grant(approval)

        