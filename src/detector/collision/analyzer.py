# src/analyzer/collision/__init__.py

"""
Module: analyzer.collision.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, TypeVar

from blueprint import Blueprint
from result import AnalysisResult
from util import LoggingLevelRouter

T = TypeVar("T")

class CollisionAnalyzer(Generic[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            target_blueprint: Blueprint[T],
            collider_candidates: List[T],
            *args,
            **kwargs,
    ) -> AnalysisResult[CollisionReport[T]]:
        pass