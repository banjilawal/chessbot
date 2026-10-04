# src/domain/metadata/unions/strcture/chart/coord/manifest.py

"""
Module: domain.metadata.unions.structure.chart.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ChartTypeUnion, CoordChart, CoordChartBlueprint
from transit import EntityCarrier

class CoordChartTypeUnion(ChartTypeUnion[CoordChart]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a CoordChart.

    Attributes:
        model: Type[CoordChart]
        carrier: Type[EntityCarrier[CoordChart]]
        blueprint: Type[CoordChartBlueprint]
        
    Provides:

    Super Class:
        CoordChartTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[CoordChart]],
            model: Optional[Type[CoordChart]] | None = None,
            blueprint: Optional[Type[CoordChartBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[CoordChart]
            carrier: Type[EntityCarrier[CoordChart]]
            blueprint: Type[CoordChartBlueprint]
        """
        super().__init__(
            model=model or CoordChart,
            blueprint=blueprint or CoordChartBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[CoordChart]:
        return cast(Type[CoordChart], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[CoordChart]]:
        return cast(Type[EntityCarrier[CoordChart]], super().carrier)
    
    @property
    def blueprint(self) -> Type[CoordChartBlueprint]:
        return cast(Type[CoordChartBlueprint], super().model)