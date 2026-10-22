# src/authorization/checker/role/attackable/checker.py

"""
Module: authorization.checker.role.attackable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from artifcat import AttackDecision
from authorization import RoleChecker
from domain import Attackable
from exchange import AttackRequest, ValidationService
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
        validation_service: ValidationService

    Provides:
        -   def execute(request: request: AttackRequest) -> AttackDecision

    Super Class:
        RoleChecker
    """
    
    def __init__(self, validation_service: ValidationService):
        """
        Args:
            validation_service: Optional[ValidationService]
        """
        super().__init__(validation_service=validation_service)
        
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        pass
 