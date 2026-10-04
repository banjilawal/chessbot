# src/transit/carrier/struct/chart/coord/carrier.py

"""
Module: transit.carrier.struct.chart.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordChart, CoordChartBlueprint
from transit import ChartCarrier


class CoordChartCarrier(ChartCarrier[CoordChart]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CoordChart its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [CoordChart | CoordChartBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CoordChartBlueprint]

    Super Class:
        ChartCarrier
    """
    
    def __init__(
            self,
            model: Optional[CoordChart] | None = None,
            blueprint: Optional[CoordChartBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CoordChart]
            blueprint: Optional[CoordChartBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[CoordChart | CoordChartBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(CoordChart, entity)
        return cast(CoordChartBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, CoordChart)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, CoordChartBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[CoordChartBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(CoordChartBlueprint, self.entity)
            return blueprint
        
        model = cast(CoordChart, self.entity)
        return CoordChartBlueprint(
            position=model.position,
            terminus=model.previous_position,
        )


    