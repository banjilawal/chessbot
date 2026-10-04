# src/transit/carrier/structure/chart/carrier.py

"""
Module: transit.carrier.structure.chart.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from domain import Chart, ParticipantChartBlueprint
from transit import StructureCarrier

T = TypeVar("T", bound="Chart")


class ChartCarrier(StructureCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Chart its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[ParticipantChartBlueprint[T]]
        entity: [T | ParticipantChartBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[ParticipantChartBlueprint[T]]

    Super Class:
        StructureCarrier
    """
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[ParticipantChartBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[ParticipantChartBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | ParticipantChartBlueprint[T]]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(T, entity)
        return cast(ParticipantChartBlueprint[T], super().entity)
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[ParticipantChartBlueprint[T]]:
        pass


    