# src/authorization/checker/applicant/promotion/checker.py

"""
Module: authorization.checker.applicant.promotion.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import ApplicantChecker
from domain import Actor
from exchange import PromotionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class PromotionApplicantChecker(ApplicantChecker[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Promotion requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: PromotionRequest) -> PromotionDecision

    Super Class:
        ApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass