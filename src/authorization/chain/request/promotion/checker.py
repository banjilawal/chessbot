# src/authorization/chain/request/promotion/checker.py

"""
Module: authorization.chain.request.promotion.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import Checker
from exchange import PromotionRequest
from util import LoggingLevelRouter

T = TypeVar("T")

class PromotionChecker(Checker[PromotionRequest], ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass