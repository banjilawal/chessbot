# src/authorization/chain/role/maneuverable/checker.py

"""
Module: authorization.chain.role.maneuverable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ManeuverDecision
from authorization import RoleChecker
from domain import Maneuverable
from exchange import ManeuverRequest, PathValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Maneuverable")

class ManeuverRoleChecker(RoleChecker[ManeuverRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Maneuverable meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: PathValidationService

    Provides:
        -   def execute(request: request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        RoleChecker
    """
    
    def __init__(self, validation_service: Optional[PathValidationService] | None = None):
        """
        Args:
            validation_service: Optional[PathValidationService]
        """
        super().__init__(validation_service=validation_service or PathValidationService())
        
    @property
    def validation_service(self) -> PathValidationService:
        return cast(PathValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass
 