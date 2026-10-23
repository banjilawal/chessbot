# src/authorization/chain/role/promotion/checker.py

"""
Module: authorization.chain.role.promotion.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import PromotionDecision
from authorization import RoleChecker
from domain import Elevateable
from exchange import PromotionRequest, RankValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevateable")

class PromotionRoleChecker(RoleChecker[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to use an Elevatable in a PromotionRequest.

    Attributes:
        validation_service : RankValidationService

    Provides:
        -   execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        RoleChecker
    """
    
    def __init__(self, validation_service : Optional[RankValidationService] | None = None):
        super().__init__(
            validation_service=validation_service or RankValidationService()
        )
        
    @property
    def validation_service(self) -> RankValidationService:
        return cast(RankValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass