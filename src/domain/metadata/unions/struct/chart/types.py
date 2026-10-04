# src/domain/metadata/unions/strcture/chart/manifest.py

"""
Module: domain.metadata.unions.struct.chart.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Chart, ChartBlueprint, StructTypeUnion
from transit import ChartCarrier

T = TypeVar("T", bound="Chart")


class ChartTypeUnion(StructTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Chart.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[ChartBlueprint[T]]
        
    Provides:

    Super Class:
        StructTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[ChartCarrier[T]],
            blueprint: Type[ChartBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[ChartBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint, carrier=carrier)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[ChartCarrier[T]]:
        return cast(Type[ChartCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[ChartBlueprint[T]]:
        return cast(Type[ChartBlueprint[T]], super().blueprint)