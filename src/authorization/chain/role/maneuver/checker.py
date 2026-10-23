# src/authorization/chain/role/maneuverable/checker.py

"""
Module: authorization.chain.role.maneuverable.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ManeuverDecision
from authorization import RoleChecker
from domain import Maneuverable
from exchange import ManeuverRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Maneuverable")

class ManeuverRoleChecker(RoleChecker[ManeuverRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization
        -   Interface

    Responsibilities:
        1.  Interface for deciding an Actionable can be used in a Maneuver.

    Attributes:
        validation_service: ValidationService

    Provides:
        -   execute(request: ManeuverRequest) -> ManeuverDecision

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
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Decide if a Maneuver can be made with an Actionable.
        Args:
            request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
          ManeuverRoleCheckerException
        """
        pass
 