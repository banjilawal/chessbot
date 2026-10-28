# src/assurance/validator/struct/chart/validator.py

"""
Module: assurance.validator.struct.chart.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from assurance import ChartValidationLoader, ChartLayerToolkit, StructValidator
from domain import Chart
from transit import ChartCarrier
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")


class ChartValidator(StructValidator[T], ABC, Generic[T]):
    """
    Role
        - Integrity Assurance Worker

    Responsibilities:
        1.  Check that a candidate is the right type of not-null EntityCarrier.
        2.  Run safety checks on structs and blueprints inside an EntityCarrier's payload.

    Attributes:
        loader: ChartLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[StructCarrier[T]]:

    Super Class:
        StructValidator
    """
    
    def __init__(self, loader: ChartValidationLoader[T]):
        """
        Args:
            loader: ChartLoader[T]
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> ChartValidationLoader[T]:
        return cast(ChartValidationLoader[T], super().loader)
    
    @property
    def toolkit(self) -> ChartLayerToolkit[T]:
        return self.loader.toolkit
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ChartCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[ChartCarrier[T]]
        Raises:
            ChartValidatorException
        """
        pass
    
    
