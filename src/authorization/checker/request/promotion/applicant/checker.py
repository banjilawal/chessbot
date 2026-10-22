# src/authorization/checker/request/promotion/.applicant/checker.py

"""
Module: authorization.checker.request.promotion.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import PromotionChecker
from domain import Actor
from exchange import PromotionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class PromotionApplicantChecker(PromotionChecker[T], ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass