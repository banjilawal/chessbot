# src/authorization/reviewer/promotion/reviewer.py

"""
Module: authorization.reviewer.promotion.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import Reviewer, ValidItemChecker
from exchange import PromotionRequest

from util import LoggingLevelRouter

T = TypeVar("T")

class PromotionReviewer(Reviewer[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_item_checker: ValidItemChecker[T]

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        Reviewer
    """
    _valid_item_checker: ValidItemChecker[T]
    
    def __init__(self, valid_item_checker: ValidItemChecker):
        """
        Args:
            valid_item_checker: ValidItemChecker
        """
        super().__init__()
        self._valid_item_checker = valid_item_checker
        
    @property
    def valid_item_checker(self) -> ValidItemChecker[T]:
        return self._valid_item_checker
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass
        