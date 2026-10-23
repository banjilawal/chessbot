# src/authorization/chain/applicant/maneuver/checker.py

"""
Module: authorization.chain.applicant.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ManeuverDecision
from authorization import ApplicantChecker
from domain import Actor
from exchange import ManeuverRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")


class ManeuverApplicantChecker(ApplicantChecker[ManeuverRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization
        -   Interface

    Responsibilities:
        1.  Interface for implementing a check on an Actor's eligibility to perform a Maneuver.

    Attributes:

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Decide if an Actor can be granted permission to a Maneuver.
        Args:
            request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
          ManeuverApplicantCheckerException
        """
        pass
