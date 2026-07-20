# src/math/math.py

"""
Module: math.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from result import ComputationResult
from util import LoggingLevelRouter

T = TypeVar("T")

class Computer(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self) -> ComputationResult:
        pass