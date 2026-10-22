# src/authorization/checker/applicant/promotion/pawn/checker.py

"""
Module: authorization.checker.applicant.promotion.pawn.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionDecision
from authorization import PromotionTokenChecker
from domain import PawnToken
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionPawnTokenChecker(PromotionTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Promotion applicant is a PawnToken.

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
        
        if not isinstance(request.applicant, PawnToken):
            return PromotionDecision.denial(
                request=request,
                exception=TypeError(
                    f"Expected PawnToken received, "
                    f"{type(request.applicant).__class__.__name__} instead."
                )
            )
        # --- Forward the work product. ---#
        applicant = cast(PawnToken, request.applicant)
        approval = PromotionRequest(
            id=request.id,
            applicant=applicant,
            activity=request.activity,
        )
        return PromotionDecision.grant(approval)
 