# src/authorization/reviewer/promotion/applicant/reviewer.py

"""
Module: authorization.reviewer.promotion.applicant.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import PromotionDecision
from authorization import (
    Attributable, CombatantReadinessChecker, DoublePromotionChecker, PromotionPawnTokenChecker,
    PromotionReviewer, PromotionRowChecker, PropertyChecker, ValidTokenChecker
)
from domain import Token
from err import ApplicantApproverException
from exchange import PromotionRequest

from util import LoggingLevelRouter


class PromotionApplicantReviewer(PromotionReviewer[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_item_checker: ValidTokenChecker
        pawn_checker: PromotionPawnTokenChecker
        promotion_row_checker: PromotionRowChecker
        readiness_checker: CombatantReadinessChecker
        double_promotion_checker: DoublePromotionChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        RPromotionReviewer
    """

    _pawn_checker: PromotionPawnTokenChecker
    _promotion_row_checker: PromotionRowChecker
    _readiness_checker: CombatantReadinessChecker
    _double_promotion_checker: DoublePromotionChecker

    
    def __init__(
            self,
            valid_item_checker: Optional[ValidTokenChecker] | None = None,
            pawn_checker: Optional[PromotionPawnTokenChecker] | None = None,
            promotion_row_checker: Optional[PromotionRowChecker] | None = None,
            readiness_checker: Optional[CombatantReadinessChecker] | None = None,
            double_promotion_checker: Optional[DoublePromotionChecker] | None = None,
    ):
        """
        Args:
            valid_item_checker: Optional[ValidTokenChecker]
            pawn_checker: Optional[PromotionPawnTokenChecker]
            promotion_row_checker: Optional[PromotionRowChecker]
            readiness_checker: Optional[CombatantReadinessChecker]
            double_promotion_checker: Optional[DoublePromotionChecker]
        """
        super().__init__(valid_item_checker=valid_item_checker or ValidTokenChecker())
        self._pawn_checker = pawn_checker or PromotionPawnTokenChecker()
        self._readiness_checker = readiness_checker or CombatantReadinessChecker()
        self._promotion_row_checker = promotion_row_checker or PromotionRowChecker()
        self._double_promotion_checker = double_promotion_checker or DoublePromotionChecker()
        
    @property
    def valid_item_checker(self) -> ValidTokenChecker:
        return cast(ValidTokenChecker, super().valid_item_checker)
    
    @property
    def checkers(self) -> List[PropertyChecker]:
        return [
            self._pawn_checker,
            self._readiness_checker,
            self._promotion_row_checker,
            self._double_promotion_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        method = f"{self.__class__.__name__}.execute"
        
        for checker in self.checkers:
            decision = checker.execute(request)
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
        approval = PromotionRequest(
            id=request.id,
            activity=request.activity,
            applicant=request.applicant,
        )
        return PromotionDecision.grant(approval)
        