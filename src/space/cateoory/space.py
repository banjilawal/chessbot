# src/space/space.py

"""
Module: space.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from result import ComputationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="TargetVectorSet")

class Space(ABC, Generic[T]):
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def target_vectors(self) -> ComputationResult[T]:
        pass