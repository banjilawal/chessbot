# src/logic/system/relation/analysis/validator.py

"""
Module: logic.system.relation.analysis.analyzer
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from system import LoggingLevelRouter
from result import ComputationResult

T = TypeVar("T")


class ComputationWorker(ABC, Generic[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(cls, *args, **kwargs) -> ComputationResult[T]:
        pass