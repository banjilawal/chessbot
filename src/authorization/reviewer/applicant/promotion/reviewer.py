# src/authorization/reviewer/applicant/promotion/reviewer.py

"""
Module: authorization.reviewer.applicant.promotion.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from artifcat import PromotionDecision
from authorization import (
    ApplicantChecker, ApplicantReadinessChecker, ApplicantReviewer,
    DoublePromotionChecker, PromotionPawnTokenChecker, PromotionRowChecker, ValidTokenChecker,
)
from err import ApplicantApproverException
from exchange import PromotionRequest

from util import LoggingLevelRouter


class PromotionApplicantReviewer(ApplicantReviewer[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_applicant_checker: ValidTokenChecker
        pawn_checker: PromotionPawnTokenChecker
        promotion_row_checker: PromotionRowChecker
        readiness_checker: ApplicantReadinessChecker
        double_promotion_checker: DoublePromotionChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        ApplicantReviewer
    """

    _pawn_checker: PromotionPawnTokenChecker
    _promotion_row_checker: PromotionRowChecker
    _readiness_checker: ApplicantReadinessChecker
    _double_promotion_checker: DoublePromotionChecker

    
    def __init__(
            self,
            valid_applicant_checker: Optional[ValidTokenChecker] | None = None,
            pawn_checker: Optional[PromotionPawnTokenChecker] | None = None,
            promotion_row_checker: Optional[PromotionRowChecker] | None = None,
            readiness_checker: Optional[ApplicantReadinessChecker] | None = None,
            double_promotion_checker: Optional[DoublePromotionChecker] | None = None,
    ):
        """
        Args:
            valid_applicant_checker: Optional[ValidTokenChecker]
            pawn_checker: Optional[PromotionPawnTokenChecker]
            promotion_row_checker: Optional[PromotionRowChecker]
            readiness_checker: Optional[ApplicantReadinessChecker]
            double_promotion_checker: Optional[DoublePromotionChecker]
        """
        super().__init__(valid_applicant_checker=valid_applicant_checker or ValidTokenChecker())
        self._pawn_checker = pawn_checker or PromotionPawnTokenChecker()
        self._readiness_checker = readiness_checker or ApplicantReadinessChecker()
        self._promotion_row_checker = promotion_row_checker or PromotionRowChecker()
        self._double_promotion_checker = double_promotion_checker or DoublePromotionChecker()
        
    @property
    def valid_applicant_checker(self) -> ValidTokenChecker:
        return cast(ValidTokenChecker, super().valid_applicant_checker)
    
    @property
    def checkers(self) -> List[ApplicantChecker]:
        return [
            self._valid_applicant_checker,
            self._pawn_checker,
            self._readiness_checker,
            self._promotion_row_checker,
            self._double_promotion_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self._valid_applicant_checker.execute(request)
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
        