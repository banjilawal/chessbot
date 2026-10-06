# src/domain/extract/struct/chart/extract.py

"""
Module: domain.extract.struct.chart.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Chart, ChartBlueprint
from transit import ChartCarrier

T = TypeVar("T", bound="Chart")

class ChartPrimeExtract(StructPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ChartValidator.

    Attributes:
        carrier: ChartCarrier[T]
        blueprint: Optional[ChartBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            reference: ChartCarrier[T],
            blueprint: Optional[ChartBlueprint[T]] | None = None,
    ):
        """
        Args:
            reference: ChartCarrier[T]
            blueprint: Optional[ChartBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ChartCarrier[T]:
        return cast(ChartCarrier[T], super().reference)
    
    @property
    def blueprint(self) -> Optional[ChartBlueprint[T]]:
        return cast(ChartBlueprint[T], super().blueprint)