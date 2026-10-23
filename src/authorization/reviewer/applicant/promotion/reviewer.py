# src/authorization/reviewer/applicant/promotion/reviewer.py

"""
Module: authorization.reviewer.applicant.promotion.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional

from artifcat import PromotionDecision
from authorization import (
    ActorChainable, ApplicantReviewer, DoublePromotionChecker, PromotionPawnTokenChecker,
    PromotionRowChecker,  ReadyTokenChecker
)
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionApplicantReviewer(ApplicantReviewer[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        ready_checker: ReadyTokenChecker
        pawn_checker: PromotionPawnTokenChecker
        promotion_row_checker: PromotionRowChecker
        readiness_checker: ApplicantReadinessChecker
        double_promotion_checker: DoublePromotionChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        ApplicantReviewer
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
        super().__init__()
        self._ready_checker=ready_checker or ReadyTokenChecker()
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
        method = f"{self.__class__.__name__}.execute"
        
        decision = self._ready_checker.execute(request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._readiness_checker.execute(approved_request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._pawn_checker.execute(approved_request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._promotion_row_checker.execute(approved_request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._double_promotion_checker.execute(approved_request)
        if decision.is_denial:
            return PromotionDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        approval = PromotionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        return PromotionDecision.grant(approval)
        