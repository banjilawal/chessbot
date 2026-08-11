# src/authorization/authorization.py

"""
Module: authorization.authorization
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from report import RequestDecision
from util import LoggingLevelRouter

T = TypeVar("T", bound="Request")

class Authorization(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> RequestDecision:
        pass