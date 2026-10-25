# src/authorization/chain/applicant/attack/checker.py

"""
Module: authorization.chain.applicant.attack.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import AttackDecision
from authorization import ApplicantChecker
from domain import Actor
from exchange import AttackPermissionRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")


class AttackApplicantChecker(ApplicantChecker[AttackPermissionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Interface for implementing a check on an Actor's eligibility to perform an Attack.

    Attributes:

    Provides:
        -   def execute(request: AttackAuthorizationRequest) -> AttackDecision

    Super Class:
        ApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackPermissionRequest) -> AttackDecision:
        """
        Decide if an Actor can be granted permission to a Attack.
        Args:
            request: AttackAuthorizationRequest
        Returns:
           AttackDecision
        Raises:
          AttackApplicantCheckerException
        """
        pass