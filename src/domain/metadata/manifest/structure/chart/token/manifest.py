# src/domain/metadata/manifest/strcture/chart/token/manifest.py

"""
Module: domain.metadata.manifest.structure.chart.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartManifest, TokenChart, TokenChartNullGroup, TokenChartTypeUnion


class TokenChartManifest(ChartManifest[TokenChart]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the TokenChart
            security lifecycle.

     Attributes:
        types: TokenChartTypeUnion
        nulls: TokenChartNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[TokenChartTypeUnion] | None = None,
            nulls: Optional[TokenChartNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TokenChartTypeUnion]
            nulls: Optional[TokenChartNullGroup]
        """
        super().__init__(
            types=types or TokenChartTypeUnion(),
            nulls=nulls or TokenChartNullGroup(),
        )

        
    @property
    def types(self) -> TokenChartTypeUnion:
        return cast(TokenChartTypeUnion, super().types)
    
    @property
    def nulls(self) -> TokenChartNullGroup:
        return cast(TokenChartNullGroup, super().nulls)