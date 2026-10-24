# src/authorization/chain/applicant/promotion/token/pawn/checker.py

"""
Module: authorization.chain.applicant.promotion.token.pawn.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import PromotionDecision
from authorization import PromotionTokenChecker
from domain import PawnToken
from err import PromotionPawnTokenCheckerException
from exchange import PromotionAuthorizationRequest
from util import LoggingLevelRouter


class PromotionPawnTokenChecker(PromotionTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can be promoted.

    Attributes:

    Provides:
        -   execute(request: PromotionAuthorizationRequest) -> PromotionDecision

    Super Class:
        PromotionTokenChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionAuthorizationRequest) -> PromotionDecision:
        """
        Decide if a Token can be promoted.

        Action:
            1.  Deny promotion if the token is not a PawnToken.
            2.  Otherwise, issue an approval.
        Args:
            request: PromotionAuthorizationRequest
        Returns:
           PromotionDecision
        Raises:
            PromotionPawnTokenCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the applicant is not a PawnToken.
        if not isinstance(request.applicant, PawnToken):
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionPawnTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionPawnTokenCheckerException.MSG,
                    err_code=PromotionPawnTokenCheckerException.ERR_CODe,
                    ex=TypeError(
                        f"Expected PawnToken received, "
                        f"{type(request.applicant).__class__.__name__} instead."
                    )
                )
            )
        # --- Prepare an approval of the actor. ---#
        applicant = cast(PawnToken, request.applicant)
        approval = PromotionAuthorizationRequest(
            id=request.id,
            applicant=applicant,
            activity=request.activity,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)