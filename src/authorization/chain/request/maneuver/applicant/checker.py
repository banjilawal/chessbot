# src/authorization/chain/request/maneuver/.applicant/checker.py

"""
Module: authorization.chain.request.maneuver.applicant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ManeuverDecision
from authorization import ActorChainable, ManeuverChecker
from domain import Actor
from exchange import ManeuverAuthorizationRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class ManeuverApplicantChecker(ManeuverChecker[T], ActorChainable, ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverAuthorizationRequest) -> ManeuverDecision:
        pass