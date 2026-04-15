# src/analyst/analyst/collision/__init__.py

"""
Module: analyst.analyst.collision.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, TypeVar

from analyst import Blueprint, CollisionReport
from result import AnalystResult
from system import LoggingLevelRouter

T = TypeVar("T")

class CollisionAnalyst(Generic[T]):
    
    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def analyze(
            cls,
            target_blueprint: Blueprint[T],
            collider_candidates: List[T],
            *args,
            **kwargs,
    ) -> AnalystResult[CollisionReport[T]]:
        pass