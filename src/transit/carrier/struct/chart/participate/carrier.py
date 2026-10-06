# src/transit/carrier/struct/chart/participate/carrier.py

"""
Module: transit.carrier.struct.chart.participate.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Participation, ParticipationBlueprint
from transit import ChartCarrier


class ParticipationCarrier(ChartCarrier[Participation]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Participation its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Participation | ParticipationBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[ParticipationBlueprint]

    Super Class:
        ChartCarrier
    """
    
    def __init__(
            self,
            model: Optional[Participation] | None = None,
            blueprint: Optional[ParticipationBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Participation]
            blueprint: Optional[ParticipationBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[Participation | ParticipationBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(Participation, entity)
        return cast(ParticipationBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, Participation)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, ParticipationBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[ParticipationBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(ParticipationBlueprint, self.entity)
            return blueprint
        
        model = cast(Participation, self.entity)
        return ParticipationBlueprint(
            victim=model.victim,
            attacker=model.attacker,
        )


    