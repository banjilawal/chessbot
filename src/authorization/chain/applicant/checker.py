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
from authorization import ActorChainable, Checker
from exchange import PermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="PermissionRequest")

class ApplicantChecker(Checker[T], ActorChainable, ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Decides if an Actor can be granted permission to an Activity.

    Attributes:

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        Checker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Decide if an Actor can be granted permission to an activity.
        Args:
            request: T
        Returns:
           Decision[T]
        Raises:
          ApplicantCheckerException
        """
        pass
