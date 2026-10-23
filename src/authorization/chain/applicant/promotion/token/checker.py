# src/authorization/chain/applicant/promotion/token/checker.py

"""
Module: authorization.chain.applicant.promotion.token.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import PromotionDecision
from authorization import PromotionApplicantChecker
from domain import Token
from exchange import PromotionRequest
from util import LoggingLevelRouter


class PromotionTokenChecker(PromotionApplicantChecker[Token], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for checking a Token attribute satisfies promotion requirements.

    Attributes:

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Decide if a Token can be granted permission to a Promotion.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionTokenCheckerException
        """
        pass