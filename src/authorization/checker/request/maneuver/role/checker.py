# src/authorization/checker/request/maneuver/.role/checker.py

"""
Module: authorization.checker.request.maneuver.role.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ManeuverDecision
from authorization import ManeuverChecker
from domain import Elevatable
from exchange import ManeuverRequest
from util import LoggingLevelRouter

T = TypeVar("T", bound="Elevatable")

class ManeuverRoleChecker(ManeuverChecker[T], ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass