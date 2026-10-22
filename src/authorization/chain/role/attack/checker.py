# src/authorization/chain/role/attackable/checker.py

"""
Module: authorization.chain.role.attackable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import AttackDecision
from authorization import RoleChecker
from domain import Attackable
from exchange import AttackRequest, ManeuverValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Attackable")

class AttackRoleChecker(RoleChecker[AttackRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies an Attackable meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: ManeuverValidationService

    Provides:
        -   def execute(request: request: AttackRequest) -> AttackDecision

    Super Class:
        RoleChecker
    """
    
    def __init__(self, validation_service: Optional[ManeuverValidationService] | None = None):
        """
        Args:
            validation_service: Optional[ManeuverValidationService]
        """
        super().__init__(validation_service=validation_service or ManeuverValidationService())
    
    @property
    def validation_service(self) -> ManeuverValidationService:
        return cast(ManeuverValidationService, super().validation_service)
        
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        pass
 