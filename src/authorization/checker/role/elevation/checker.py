# src/authorization/checker/role/elevatable/checker.py

"""
Module: authorization.checker.role.elevatable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import RoleChecker
from domain import Elevatable
from exchange import PromotionRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevatable")

class PromotionRoleChecker(RoleChecker[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Elevatable meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: RankValidationService

    Provides:
        -   def execute(request: request: PromotionRequest) -> PromotionDecision

    Super Class:
        RoleChecker
    """
    _validation_service: ValidationService
    
    def __init__(self, validation_service: ValidationService):
        """
        Args:
            validation_service: Optional[RankValidationService]
        """
        super().__init__()
        self._validation_service = validation_service
        
    @property
    def validation_service(self) -> ValidationService:
        return self._validation_service
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass
 