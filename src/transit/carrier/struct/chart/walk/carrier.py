# src/transit/carrier/struct/chart/footstep/carrier.py

"""
Module: transit.carrier.struct.chart.footstep.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Footstep, FootstepBlueprint
from transit import ChartCarrier


class FootstepCarrier(ChartCarrier[Footstep]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Footstep its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Footstep | FootstepBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[FootstepBlueprint]

    Super Class:
        ChartCarrier
    """
    
    def __init__(
            self,
            model: Optional[Footstep] | None = None,
            blueprint: Optional[FootstepBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Footstep]
            blueprint: Optional[FootstepBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[Footstep | FootstepBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(Footstep, entity)
        return cast(FootstepBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, Footstep)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, FootstepBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[FootstepBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(FootstepBlueprint, self.entity)
            return blueprint
        
        model = cast(Footstep, self.entity)
        return FootstepBlueprint(
            position=model.position,
            terminus=model.previous_position,
        )


    