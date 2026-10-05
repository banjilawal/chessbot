# src/transit/carrier/struct/chart/walk/carrier.py

"""
Module: transit.carrier.struct.chart.walk.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Walk, WalkBlueprint
from transit import ChartCarrier


class WalkCarrier(ChartCarrier[Walk]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Walk its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Walk | WalkBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[WalkBlueprint]

    Super Class:
        ChartCarrier
    """
    
    def __init__(
            self,
            model: Optional[Walk] | None = None,
            blueprint: Optional[WalkBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Walk]
            blueprint: Optional[WalkBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[Walk | WalkBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(Walk, entity)
        return cast(WalkBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, Walk)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, WalkBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[WalkBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(WalkBlueprint, self.entity)
            return blueprint
        
        model = cast(Walk, self.entity)
        return WalkBlueprint(
            position=model.position,
            terminus=model.previous_position,
        )


    