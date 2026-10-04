# src/domain/metadata/nulls/structure/chart/group.py

"""
Module: domain.metadata.nulls.structure.chart.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Chart, StructureNullGroup
from err import (
    ChartBlueprintNullException, ChartCarrierNullException, ChartNullException
)

T = TypeVar("T", bound="Chart")

class ChartNullGroup(StructureNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Chart's integrity cycle.

    Attributes:
        model: ChartNullException
        carrier: ChartCarrierNullException
        blueprint: ChartBlueprintNullException

    Provides:

    Super Class:
        StructureNullGroup
    """

    
    def __init__(
            self,
            model: ChartNullException,
            carrier: ChartCarrierNullException,
            blueprint: ChartBlueprintNullException,
    ):
        """
        Args:
            model: ChartNullException
            carrier: ChartCarrierNullException
            blueprint: ChartBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
        
    @property
    def structure(self) -> ChartNullException:
        return cast(ChartNullException, super().model)
    
    @property
    def model(self) -> ChartNullException:
        return self.structure
    
    @property
    def carrier(self) -> ChartCarrierNullException:
        return cast(ChartCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ChartBlueprintNullException:
        return cast(ChartBlueprintNullException, super().blueprint)