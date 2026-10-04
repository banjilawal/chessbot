# src/domain/metadata/nulls/structure/chart/coord/group.py

"""
Module: domain.metadata.nulls.structure.chart.coord.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartNullGroup, CoordChart
from err import (
    CoordChartBlueprintNullException, CoordChartCarrierNullException,
    CoordChartNullException
)


class CoordChartNullGroup(ChartNullGroup[CoordChart]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CoordChart's integrity cycle.

    Attributes:
        model: CoordChartNullException
        carrier: CoordChartCarrierNullException
        blueprint:CoordChartBlueprintNullException

    Provides:

    Super Class:
        ChartNullGroup
    """

    
    def __init__(
            self,
            model: Optional[CoordChartNullException] | None = None,
            carrier: Optional[CoordChartCarrierNullException] | None = None,
            blueprint: Optional[CoordChartBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CoordChartNullException]
            carrier: Optional[CoordChartCarrierNullException]
            blueprint: Optional[CoordChartBlueprintNullException]
        """
        super().__init__(
            model=model or CoordChartNullException(),
            carrier=carrier or CoordChartCarrierNullException(),
            blueprint=blueprint or CoordChartBlueprintNullException(),
        )
        
    @property
    def structure(self) -> CoordChartNullException:
        return cast(CoordChartNullException, super().model)
    
    @property
    def model(self) -> CoordChartNullException:
        return self.structure
    
    @property
    def carrier(self) -> CoordChartCarrierNullException:
        return cast(CoordChartCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CoordChartBlueprintNullException:
        return cast(CoordChartBlueprintNullException, super().blueprint)