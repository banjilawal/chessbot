# src/assurance/load/struct/chart/loader.py

"""
Module: assurance.load.struct.chart.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ChartValidatorToolkit, StructLoader
from domain import Chart, ChartPrimeExtract
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")

class ChartLoader(StructLoader[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   ChartValidationRequest[T]
            -   ChartCarrier[T]
            -   ChartBlueprint[T]

    Attributes:

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[ChartPrimeExtract[T]

    Super Class:
        Loader
    """
    
    def __init__(self, toolkit: ChartValidatorToolkit[T]):
        """
        Args:
            toolkit: ValidatorToolkit[T]
        """
        super().__init__(toolkit=toolkit)
    
    @property
    def toolkit(self) -> ChartValidatorToolkit[T]:
        return cast(ChartValidatorToolkit[T], super().toolkit)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[ChartPrimeExtract[T]]:
        """
        Extract a safe ChartBlueprint from the candidate.
        Args:
            candidate: Any
        Returns:
            ValidationResult[ChartBlueprint[T]]
        Raises:
            ChartExtractorException
        """
        pass