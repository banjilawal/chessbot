# src/authorization/checker/applicant/promotion/checker.py

"""
Module: authorization.checker.applicant.promotion.checker
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
        1.  Checks that an applicant satisfies one of the Promotion requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: PromotionRequest) -> PromotionDecision

    Super Class:
        PromotionApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass