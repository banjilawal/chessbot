# src/logic/system/relation/analysis/analyzer.py

"""
Module: logic.system.relation.analysis.analyzer
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from logic.system import LoggingLevelRouter
from logic.system.computation import ComputationResult


T = TypeVar("T")


class Computer(ABC, Generic[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def compute(cls, *args, **kwargs) -> ComputationResult[T]:
        pass