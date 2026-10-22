# src/authorization/chain/request/maneuver/checker.py

"""
Module: authorization.chain.request.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import ManeuverDecision
from authorization import Checker
from exchange import ManeuverRequest
from util import LoggingLevelRouter

T = TypeVar("T")

class ManeuverChecker(Checker[ManeuverRequest], ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        pass