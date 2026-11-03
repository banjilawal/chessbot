# src/authorization/chain/applicant/checker.py

"""
Module: authorization.chain.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import Decision
from authorization import ActorChainable, RoleChecker
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class ApplicantChecker(RoleChecker[T], ActorChainable, ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Decides if an Actor can be granted permission to an Activity.

    Attributes:

    Provides:
        -   def execute(candidate: Any) -> Decision

    Super Class:
        Checker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> Decision:
        """
        Decide if an Actor can be granted permission to an activity.
        Args:
            candidate: Any
        Returns:
           Decision
        Raises:
          ApplicantCheckerException
        """
        pass
