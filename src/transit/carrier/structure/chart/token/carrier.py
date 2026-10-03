# src/transit/carrier/structure/chart/token/carrier.py

"""
Module: transit.carrier.structure.chart.token.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TokenChart, TokenChartBlueprint
from transit import ChartCarrier


class TokenChartCarrier(ChartCarrier[TokenChart]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated TokenChart its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [TokenChart | TokenChartBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[TokenChartBlueprint]

    Super Class:
        ChartCarrier
    """
    
    def __init__(
            self,
            model: Optional[TokenChart] | None = None,
            blueprint: Optional[TokenChartBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[TokenChart]
            blueprint: Optional[TokenChartBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[TokenChart | TokenChartBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(TokenChart, entity)
        return cast(TokenChartBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, TokenChart)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, TokenChartBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[TokenChartBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(TokenChartBlueprint, self.entity)
            return blueprint
        
        model = cast(TokenChart, self.entity)
        return TokenChartBlueprint(
            victim=model.victim,
            attacker=model.attacker,
        )


    