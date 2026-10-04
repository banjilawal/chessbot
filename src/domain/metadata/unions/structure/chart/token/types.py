# src/domain/metadata/unions/strcture/chart/token/manifest.py

"""
Module: domain.metadata.unions.structure.chart.token.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import ChartTypeUnion, TokenChart, TokenChartBlueprint
from transit import EntityCarrier

class TokenChartTypeUnion(ChartTypeUnion[TokenChart]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a TokenChart.

    Attributes:
        model: Type[TokenChart]
        carrier: Type[EntityCarrier[TokenChart]]
        blueprint: Type[TokenChartBlueprint]
        
    Provides:

    Super Class:
        TokenChartTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[TokenChart]],
            model: Optional[Type[TokenChart]] | None = None,
            blueprint: Optional[Type[TokenChartBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[TokenChart]
            carrier: Type[EntityCarrier[TokenChart]]
            blueprint: Type[TokenChartBlueprint]
        """
        super().__init__(
            model=model or TokenChart,
            blueprint=blueprint or TokenChartBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[TokenChart]:
        return cast(Type[TokenChart], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[TokenChart]]:
        return cast(Type[EntityCarrier[TokenChart]], super().carrier)
    
    @property
    def blueprint(self) -> Type[TokenChartBlueprint]:
        return cast(Type[TokenChartBlueprint], super().model)