# src/transit/carrier/model/encounter/stalemate/carrier.py

"""
Module: transit.carrier.model.encounter.stalemate.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StalemateEncounter, StalemateEncounterBlueprint
from transit import EncounterCarrier


class StalemateEncounterCarrier(EncounterCarrier[StalemateEncounter]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated StalemateEncounter or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [StalemateEncounter | StalemateEncounterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[StalemateEncounterBlueprint]

    Super Class:
        EncounterCarrier
    """
    
    def __init__(
            self,
            model: Optional[StalemateEncounter] | None = None,
            blueprint: Optional[StalemateEncounterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[StalemateEncounter]
            blueprint: Optional[StalemateEncounterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[StalemateEncounter | StalemateEncounterBlueprint]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, StalemateEncounter)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, StalemateEncounterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[StalemateEncounterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(StalemateEncounter, self._model)
        return StalemateEncounterBlueprint(
            id=model.id,
            victim=model.victim,
            attacker_maneuver=model.attacker_maneuver,
        )


