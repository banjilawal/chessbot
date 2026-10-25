# src/authorization/chain/applicant/promotion/checker.py

"""
Module: authorization.chain.applicant.promotion.checker
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
from exchange import PromotionPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")


class PromotionApplicantChecker(ApplicantChecker[PromotionPermissionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for implementing a check on an Actor's eligibility for Promotion.

    Attributes:

    Provides:
        -   def execute(request: PromotionAuthorizationRequest) -> PromotionDecision

    Super Class:
        ApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Decide if an Actor can be granted permission to a Promotion.
        Args:
            request: PromotionAuthorizationRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionApplicantCheckerException
        """
        pass
