# src/exchange/wrapper/validation/structure/chart/wrapper.py

"""
Module: exchange.wrapper.validation.structure.chart.wrapper
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
    ChartValidationRequest, ChartValidationResponder, StructureValidationResponseWrapper,
)
from util import LoggingLevelRouter

T = TypeVar("T", bound="Chart")

class ChartValidationResponseWrapper(
    StructureValidationResponseWrapper[T],
    ABC,
    Generic[T]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract the either:
                -   The Chart
                _   The Blueprint
            from a ChartValidationResponse.

    Attributes:
        responder: ChartValidationResponder[T]
        
    Provides:
        -   def extract_chart(
                    self,
                    request: ChartValidationRequest[T]
            ) -> ValidationResult[T]
            
        -   def extract_blueprint(
                    self,
                    request: ChartValidationRequest[T]
            ) -> ValidationResult[Blueprint[T]]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(self, responder: ChartValidationResponder[T]):
        """
        Args:
            responder: ChartValidationResponder[T]
        """
        super().__init__(responder=responder)
    
    @property
    def responder(self) -> ChartValidationResponder[T]:
        return cast(ChartValidationResponder[T], super().responder)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_chart(
            self,
            request: ChartValidationRequest[T]
    ) -> ValidationResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def extract_chart(
            self,
            request: ChartValidationRequest[T]
    ) -> ValidationResult[ChartBlueprint[T]]:
        pass