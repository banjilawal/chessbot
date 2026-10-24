# src/authorization/chain/applicant/promotion/token/row/checker.py

"""
Module: authorization.chain.applicant.promotion.token.row.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from artifcat import PromotionDecision
from authorization import PromotionTokenChecker
from err import PromotionRowException
from exchange import PromotionRequest
from util import LoggingLevelRouter

class PromotionRowChecker(PromotionTokenChecker):
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
            1.  Deny promotion if the token does not occupy its
                promotion row.
            2.  Otherwise, issue an approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionRowCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the actor does not occupy the promotion_row.
        promotion_row = request.applicant.team.enemy_rank_row
        position = request.applicant.footstep.position
        
        if position is None or position.row != promotion_row:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionRowException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionRowException.MSG,
                    err_code=PromotionRowException.ERR_CODE,
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