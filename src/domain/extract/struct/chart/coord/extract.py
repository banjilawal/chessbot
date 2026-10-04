# src/domain/extract/struct/chart/coord.extract.py

"""
Module: domain.extract.struct.chart.coord.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordChart, CoordChartBlueprint, ChartPrimeExtract
from transit import CoordChartCarrier


class CoordChartPrimeExtract(ChartPrimeExtract[CoordChart]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CoordChartValidator.

    Attributes:
        carrier: CoordChartCarrier
        blueprint: Optional[CoordChartBlueprint]

    Provides:

    Super Class:
        ChartPrimeExtract
    """

    def __init__(
            self,
            carrier: CoordChartCarrier,
            blueprint: Optional[CoordChartBlueprint] | None = None,
    ):
        """
        Args:
            carrier: CoordChartCarrier
            blueprint: Optional[CoordChartBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> CoordChartCarrier:
        return cast(CoordChartCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[CoordChartBlueprint]:
        return cast(CoordChartBlueprint, super().blueprint)