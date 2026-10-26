# src/exchange/service/validation/struct/chart/service.py

"""
Module: exchange.service.validation.struct.chart.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Chart, ChartBlueprint
from exchange import (
    ChartValidationRequest, ChartValidationService, StructValidationService,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")

class ChartValidationService(
    StructValidationService[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract the either:
                -   The Chart
                _   The Blueprint
            from a ChartValidationResponse.

    Attributes:
        service: ChartValidationService[T]
        
    Provides:
        -   def extract_model(
                    self,
                    request: ChartValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: ChartValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationService
    """
    
    def __init__(self, service: ChartValidationService[T]):
        """
        Args:
            service: ChartValidationService[T]
        """
        super().__init__(service=service)
    
    @property
    def service(self) -> ChartValidationService[T]:
        return cast(ChartValidationService[T], super().service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ChartValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_model(
            self,
            request: ChartValidationRequest[T]
    ) -> ValidationResult[ChartBlueprint[T]]:
        pass