# src/authorization/role/promotion/permitter.py

"""
Module: authorization.role.promotion.permitter
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import PromotionDecision
from authorization import RolePermitter
from domain import Elevatable
from exchange import PromotionPermissionRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevatable")

class PromotionRolePermitter(RolePermitter[PromotionPermissionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for deciding an Actionable can be used in a Promotion.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   execute(request: PromotionAuthorizationRequest) -> PromotionDecision

    Super Class:
        RolePermitter
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
    def execute(self, request: PromotionPermissionRequest) -> PromotionDecision:
        """
        Decide if a Promotion can be made with an Actionable.
        Args:
            request: PromotionAuthorizationRequest
        Returns:
           PromotionDecision
        Raises:
          PromotionRolePermitterException
        """
        pass