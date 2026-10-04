# src/domain/extract/struct/chart/token.extract.py

"""
Module: domain.extract.struct.chart.token.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TokenChart, TokenChartBlueprint, ChartPrimeExtract
from transit import TokenChartCarrier


class TokenChartPrimeExtract(ChartPrimeExtract[TokenChart]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TokenChartValidator.

    Attributes:
        carrier: TokenChartCarrier
        blueprint: Optional[TokenChartBlueprint]

    Provides:

    Super Class:
        ChartPrimeExtract
    """

    def __init__(
            self,
            carrier: TokenChartCarrier,
            blueprint: Optional[TokenChartBlueprint] | None = None,
    ):
        """
        Args:
            carrier: TokenChartCarrier
            blueprint: Optional[TokenChartBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> TokenChartCarrier:
        return cast(TokenChartCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[TokenChartBlueprint]:
        return cast(TokenChartBlueprint, super().blueprint)