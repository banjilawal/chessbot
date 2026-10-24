# src/authorization/role/attackable/permitter.py

"""
Module: authorization.role.attackable.permitter
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import AttackDecision
from authorization import RolePermitter
from domain import Attackable
from exchange import AttackRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Attackable")

class AttackRolePermitter(RolePermitter[AttackRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for deciding an Actionable can be used in an Attack.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   execute(request: AttackRequest) -> AttackDecision

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
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Decide if an Attack can be made with an Actionable.
        Args:
            request: AttackRequest
        Returns:
           AttackDecision
        Raises:
          AttackRolePermitterException
        """
        pass
 