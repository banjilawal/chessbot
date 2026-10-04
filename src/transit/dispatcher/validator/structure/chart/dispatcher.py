# src/transit/dispatcher/validator/structure/chart/validator.py

"""
Module: transit.dispatcher.validator.chart.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from assurance import ChartValidator
from artifcat import ValidationResult
from domain import Chart
from transit import ChartCarrier, StructureValidationDispatcher
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")

class ChartValidationDispatcher(StructureValidationDispatcher[T], ABC, Generic[T]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Validation Process Owner

    Responsibilities:
        1.  Ensure a Model instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: ChartValidator[T]
        
    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult

    Super Class:
        Validator
    """
    
    def __init__(self, validator: ChartValidator[T]):
        super().__init__(validator=validator)
    
    @property
    def validator(self) -> ChartValidator:
        return cast(ChartValidator[T], super().validator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ChartCarrier[T]]:
        pass
    
        
        
