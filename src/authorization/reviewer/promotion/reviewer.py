# src/authorization/reviewer/promotion/reviewer.py

"""
Module: authorization.reviewer.promotion.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar, cast

from artifcat import PromotionDecision
from authorization import ActorChainable, ApplicantReviewer, ReadyChecker
from domain import Actor
from exchange import PromotionPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class PromotionApplicantReviewer(ApplicantReviewer[PromotionPermissionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for implementing a Promotion applicant permission check chain.

    Attributes:
        ready_checker: ReadyChecker[T]
        checkers: List[ActorChainable]

    Provides:
        -   def execute(request: PromotionAuthorizationRequest) -> PromotionDecision

    Super Class:
        ApplicantReviewer
    """
    
    def __init__(self, ready_checker: ReadyChecker):
        """
        Args:
            ready_checker: ReadyChecker
        """
        super().__init__(ready_checker=ready_checker)
        
    @property
    def ready_checker(self) -> ReadyChecker[T]:
        return cast(ReadyChecker[T], super().ready_checker)
    
    @property
    @abstractmethod
    def checkers(self) -> List[ActorChainable]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Decide if an applicant can be promoted.
        Args:
            request: PromotionAuthorizationRequest
        Returns:
            PromotionDecision
        Raises:
            PromotionApplicantReviewerException
        """
        pass

        