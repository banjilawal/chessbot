# src/authorization/role/maneuverable/checker.py

"""
Module: authorization.role.maneuverable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ManeuverDecision
from authorization import RolePermitter
from domain import Maneuverable
from exchange import ManeuverAuthorizationRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Maneuverable")

class ManeuverRolePermitter(RolePermitter[ManeuverAuthorizationRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for deciding an Actionable can be used in a Maneuver.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   execute(request: ManeuverAuthorizationRequest) -> ManeuverDecision

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
    def execute(self, request: ManeuverAuthorizationRequest) -> ManeuverDecision:
        """
        Decide if a Maneuver can be made with an Actionable.
        Args:
            request: ManeuverAuthorizationRequest
        Returns:
           ManeuverDecision
        Raises:
          ManeuverRoleCheckerException
        """
        pass
 