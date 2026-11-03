# src/authorization/checker/maneuver/checker.py

"""
Module: authorization.checker.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import ManeuverDecision
from authorization import RoleChecker
from domain import Path, Token
from exchange import ManeuverPermissionRequest, ManeuverRequest
from util import LoggingLevelRouter


class ManeuverPathChecker(RoleChecker[ManeuverDecision, Token, Path], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check that a Token and Path satisfy the ManeuverTransaction requirements.

    Attributes:

    Provides:
        -   def execute(
                    principal: Token,
                    role: Path,
                    transaction_request: ManeuverRequest,
                    permission_request: ManeuverPermissionRequest,
            ) -> ManeuverDecision

    Super Class:
        RoleChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(
            self,
            role: Path,
            principal: Token,
            transaction_request: ManeuverRequest,
            permission_request: ManeuverPermissionRequest,
    ) -> ManeuverDecision:
        """
        Decide if an Actor can be granted permission to a Maneuver.
        Args:
            role: Path
            principal: Token
            transaction_request: ManeuverRequest
            permission_request: ManeuverPermissionRequest
        Returns:
            ManeuverDecision
        Raises:
            ManeuverPathCheckerException
        """
        pass
