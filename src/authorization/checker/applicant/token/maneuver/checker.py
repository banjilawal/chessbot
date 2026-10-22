# src/authorization/checker/applicant/token/maneuver/checker.py

"""
Module: authorization.checker.applicant.token.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import ManeuverDecision
from authorization import TokenApplicantChecker
from exchange import ManeuverRequest
from util import LoggingLevelRouter


class ManeuverApplicantChecker(TokenApplicantChecker[ManeuverRequest], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Maneuver requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        TokenApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass