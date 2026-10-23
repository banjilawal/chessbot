# src/authorization/reviewer/promotion/token/reviewer.py

"""
Module: authorization.reviewer.promotion.token.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional

from artifcat import PromotionDecision
from authorization import (
    ActorChainable, DoublePromotionChecker, PromotionApplicantReviewer, PromotionPawnTokenChecker,
    PromotionRowChecker, ReadyTokenChecker,
)
from domain import Token
from err import PromotionTokenReviewerException
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionTokenReviewer(PromotionApplicantReviewer[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can be promoted.

    Attributes:
        ready_checker: ReadyTokenChecker
        pawn_checker: PromotionPawnTokenChecker
        promotion_row_checker: PromotionRowChecker
        double_promotion_checker: DoublePromotionChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionApplicantReviewer
    """
    _ready_checker: ReadyTokenChecker
    _pawn_checker: PromotionPawnTokenChecker
    _promotion_row_checker: PromotionRowChecker
    _double_promotion_checker: DoublePromotionChecker
    
    def __init__(
            self,
            ready_checker: Optional[ReadyTokenChecker] | None = None,
            pawn_checker: Optional[PromotionPawnTokenChecker] | None = None,
            promotion_row_checker: Optional[PromotionRowChecker] | None = None,         
            double_promotion_checker: Optional[DoublePromotionChecker] | None = None,
    ):
        """
        Args:
            ready_checker: Optional[ReadyTokenChecker]
            pawn_checker: Optional[PromotionPawnTokenChecker]
            promotion_row_checker: Optional[PromotionRowChecker]
            double_promotion_checker: Optional[DoublePromotionChecker]
        """
        super().__init__(ready_checker=ready_checker or ReadyTokenChecker())
        self._pawn_checker = pawn_checker or PromotionPawnTokenChecker()
        self._promotion_row_checker = promotion_row_checker or PromotionRowChecker()
        self._double_promotion_checker = double_promotion_checker or DoublePromotionChecker()
    
    @property
    def checkers(self) -> List[ActorChainable]:
        return [
            self._ready_checker,
            self._pawn_checker,
            self._promotion_row_checker,
            self._double_promotion_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Decide if a Token can be promoted
        
        Action:
        Args:
            request: PromotionRequest
        Returns:
            PromotionDecision
        Raises:
            PromotionTokenReviewerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the token is not ready.
        decision = self._ready_checker.execute(request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionTokenReviewerException.MSG,
                    err_code=PromotionTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the pawn_checker does not grant permission.
        approved_request = decision.request
        decision = self._pawn_checker.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionTokenReviewerException.MSG,
                    err_code=PromotionTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the row_checker does not grant permission.
        approved_request = decision.request
        decision = self._promotion_row_checker.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionTokenReviewerException.MSG,
                    err_code=PromotionTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the double_promotion_checker does not grant permission.
        approved_request = decision.request
        decision = self._double_promotion_checker.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return PromotionDecision.denial(
                request=request,
                exception=PromotionTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PromotionTokenReviewerException.MSG,
                    err_code=PromotionTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approved_request = decision.request
        approval = PromotionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return PromotionDecision.grant(approval)

        