# src/authorization/applicant/token/promotion/approver.py

"""
Module: authorization.applicant.token.promotion.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast
from wsgiref.validate import check_exc_info

from artifcat import PromotionDecision
from authorization import (
    CombatantReadinessChecker, DoublePromotionChecker, PromotionAuthorizationLoader,
    PromotionLoadChecker, RankElevatableChecker, TokenApprover
)
from domain import PawnToken, Token
from err import DisabledPawnPromotionException, TokenPromotionApproverException
from exchange import PromotionRequest, TokenValidationService
from logic.promotion.promotion.exception import DoublePromotionException
from util import LoggingLevelRouter


class TokenPromotionApprover(TokenApprover[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:
        validation_service: TokenValidationService
        loader: Optional[PromotionAuthorizationLoader]

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        TokenApprover
    """
    _row_checker: RankElevatableChecker
    _double_checker: DoublePromotionChecker
    _readiness_checker: CombatantReadinessChecker
    _load_checker: PromotionLoadChecker
    
    def __init__(
            self,
            row_checker: Optional[RankElevatableChecker] | None = None,
            double_checker: Optional[DoublePromotionChecker] | None = None,
            readiness_checker: Optional[CombatantReadinessChecker] | None = None,
            load_checker: Optional[PromotionLoadChecker] | None = None,
            validation_service: Optional[TokenValidationService] | None = None,
            loader: Optional[PromotionAuthorizationLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PromotionAuthorizationLoader]
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(
            loader=loader or PromotionAuthorizationLoader(),
            validation_service=validation_service or TokenValidationService(),
        )
        self._row_checker = row_checker or RankElevatableChecker()
        self._double_checker = double_checker or DoublePromotionChecker()
        self._readiness_checker = readiness_checker or CombatantReadinessChecker()
        self._load_checker = load_checker or PromotionLoadChecker()
        
    @property
    def loader(self) -> PromotionAuthorizationLoader:
        return cast(PromotionAuthorizationLoader, super().loader)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Checks if a Token meets the requirements to perform an activity.
        
        Action:
            1.  Return Promotion denial if any of the following occur:
                    -   The request is either null or the wrong type.
                    -   The applicant is not a PawnToken.
                    -   The applicant is not ready.
                    -   The applicant has already been promoted.
                    -   The actor is not on its enemy's rank row.
            2.  Otherwise, send a promotion approval.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            TokenPromotionApproverException
        """
        method = f"{self.__class__.__name__}"
        
        decision = PromotionDecision.denial(
            request,
            TokenPromotionApproverException(),
        )
        for checker in [
            self._load_checker,
            self._readiness_checker,
            self._row_checker,
            self._double_checker,
        ]:
            decision = checker.execute(request)
            if decision.is_denied:
                return PromotionDecision.denial(
                    request=request,
                    exception=TokenPromotionApproverException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPromotionApproverException.MSG,
                        err_code=TokenPromotionApproverException.ERR_CODE,
                        ex=decision.exception
                    ),
                )
        checked_request = cast(PromotionRequest, decision.request)
        approval = PromotionRequest(
            id=checked_request.id,
            activity=checked_request.activity,
            applicant=checked_request.applicant,
        )
        return PromotionDecision.grant(approval)
        
        