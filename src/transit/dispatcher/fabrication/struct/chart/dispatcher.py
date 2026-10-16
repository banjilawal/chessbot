# src/transit/dispatcher/fabrication/struct/chart/dispatcher.py

"""
Module: transit.dispatcher.fabrication.chart.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from fabrication import ChartBuilder
from artifcat import BuildResult
from domain import Chart
from transit import ChartCarrier, StructBuildDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")

class ChartBuildDispatcher(StructBuildDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Build Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: ChartBuilder[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> BuildResult

    Super Class:
        Builder
    """
    
    def __init__(self, builder: ChartBuilder[T]):
        super().__init__(builder=builder)
    
    @property
    def builder(self) -> ChartBuilder:
        return cast(ChartBuilder[T], super().builder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ChartCarrier[T]]:
        pass
    
        
        
