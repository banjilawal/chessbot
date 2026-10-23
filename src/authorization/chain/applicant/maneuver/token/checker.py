# src/authorization/chain/applicant/maneuver/token/checker.py

"""
Module: authorization.chain.applicant.maneuver.token.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from artifcat import ManeuverDecision
from authorization import ManeuverApplicantChecker
from domain import Token
from exchange import ManeuverRequest
from util import LoggingLevelRouter


class ManeuverTokenChecker(ManeuverApplicantChecker[Token], ABC):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Maneuver requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ManeuverApplicantChecker
    """
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass