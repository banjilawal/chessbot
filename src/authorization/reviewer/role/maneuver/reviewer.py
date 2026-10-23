# src/authorization/reviewer/role/maneuver/reviewer.py

"""
Module: authorization.reviewer.role.maneuver.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import ManeuverDecision
from authorization import ManeuverPathChecker, RoleReviewer
from domain import Elevateable
from exchange import ManeuverRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevateable")


class ManeuverRoleReviewer(RoleReviewer[ManeuverRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        checker: PathChecker

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        RoleReviewer
    """
    
    def __init__(self, checker: Optional[ManeuverPathChecker] | None = None):
        """
        Args:
            checker: Optional[ManeuverPathChecker]
        """
        super().__init__(checker=checker or ManeuverPathChecker())

    @property
    def checker(self) -> ManeuverPathChecker:
        return cast(ManeuverPathChecker, super().checker)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass