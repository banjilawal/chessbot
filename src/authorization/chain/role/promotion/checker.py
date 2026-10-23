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
from exchange import PromotionRequest, RankValidationService, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevateable")

class PromotionRoleChecker(RoleChecker[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for deciding an Actionable can be used in a Promotion.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        RoleChecker
    """
    
    def __init__(self, validation_service: ValidationService):
        """
        Args:
            validation_service: ValidationService
        """
        super().__init__(validation_service=validation_service)
    
    @property
    def validation_service(self) -> ValidationService:
        return cast(ValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        """
        Decide if an Promotion can be made with an Actionable.
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionRoleCheckerException
        """
        pass