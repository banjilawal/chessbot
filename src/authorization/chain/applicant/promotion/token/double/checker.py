# src/authorization/chain/applicant/promotion/token/double/checker.py

"""
Module: authorization.chain.applicant.promotion.token.double.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import PromotionDecision
from authorization import PromotionTokenChecker
from err import DoublePromotionException
from exchange import PromotionRequest
from util import LoggingLevelRouter


class DoublePromotionChecker(PromotionTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can be promoted.

    Attributes:

    Provides:
        -   execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionTokenChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Decide if a Token can be promoted.

        Action:
            1.  Deny promotion if the token has already been promoted.
            2.  Otherwise, issue an approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            DoublePromotionCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the applicant has already been promoted.
        if request.applicant.is_promoted:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=DoublePromotionException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DoublePromotionException.MSG,
                    err_code=DoublePromotionException.ERR_CODE,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approval = PromotionRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)
    

 