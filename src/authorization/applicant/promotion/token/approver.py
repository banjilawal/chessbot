# src/authorization/applicant/promotion/token/approver.py

"""
Module: authorization.applicant.promotion.token.approver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PromotionDecision
from authorization import PromotionApplicantApprover
from domain import Token
from exchange import PromotionRequest, TokenValidationService
from util import LoggingLevelRouter


class TokenPromotionApplicantApprover(PromotionApplicantApprover[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Reports if a Token can apply for a Promotion.

    Attributes:
        validation_service: TokenValidationService

    Provides:
        -   def execute(self, request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionApplicantApprover
    """
    
    def __init__(self, validation_service: Optional[TokenValidationService] | None = None):
        """
        Args:
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(validation_service=validation_service or TokenValidationService())
    
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass

        