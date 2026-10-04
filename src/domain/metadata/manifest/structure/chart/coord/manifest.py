# src/domain/metadata/manifest/strcture/chart/coord/manifest.py

"""
Module: domain.metadata.manifest.structure.chart.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartManifest, CoordChart, CoordChartNullGroup, CoordChartTypeUnion


class CoordChartManifest(ChartManifest[CoordChart]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the CoordChart
            security lifecycle.

     Attributes:
        types: CoordChartTypeUnion
        nulls: CoordChartNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[CoordChartTypeUnion] | None = None,
            nulls: Optional[CoordChartNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CoordChartTypeUnion]
            nulls: Optional[CoordChartNullGroup]
        """
        super().__init__(
            types=types or CoordChartTypeUnion(),
            nulls=nulls or CoordChartNullGroup(),
        )

        
    @property
    def types(self) -> CoordChartTypeUnion:
        return cast(CoordChartTypeUnion, super().types)
    
    @property
    def nulls(self) -> CoordChartNullGroup:
        return cast(CoordChartNullGroup, super().nulls)