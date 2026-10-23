# src/authorization/reviewer/role/promotion/reviewer.py

"""
Module: authorization.reviewer.role.promotion.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import PromotionDecision
from authorization import PromotionRankChecker, RoleReviewer
from domain import Elevateable
from exchange import PromotionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevateable")


class PromotionRoleReviewer(RoleReviewer[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        checker: RankChecker

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        RoleReviewer
    """
    
    def __init__(self, checker: Optional[PromotionRankChecker] | None = None):
        """
        Args:
            checker: Optional[PromotionRankChecker]
        """
        super().__init__(checker=checker or PromotionRankChecker())

    @property
    def checker(self) -> PromotionRankChecker:
        return cast(PromotionRankChecker, super().checker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass