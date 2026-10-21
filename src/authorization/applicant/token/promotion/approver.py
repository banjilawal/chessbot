# src/authorization/applicant/token/promotion/approver.py

"""
Module: authorization.applicant.token.promotion.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import PromotionDecision
from authorization import TokenApprover
from exchange import PromotionRequest, TokenValidationService
from util import LoggingLevelRouter


class TokenPromotionApprover(TokenApprover[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:
        validation_service: TokenValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        TokenApprover
    """

    
    def __init__(
            self,
            validation_service: Optional[TokenValidationService] | None = None
    ):
        """
        Args:
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(
            validation_service=validation_service or TokenValidationService()
        )
    

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
            TokenPromotionApprover
        """
        pass
        