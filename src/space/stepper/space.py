# src/space/interval/space.py

"""
Module: space.interval.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic

from result import ComputationResult
from util import LoggingLevelRouter


T = TYpeVar("T", bound="Space")


class Stepper(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def next(self) -> ComputationResult:
        pass