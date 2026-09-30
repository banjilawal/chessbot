# src/transit/carrier/model/encounter/kill/carrier.py

"""
Module: transit.carrier.model.encounter.kill.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KillEncounter, KillEncounterBlueprint
from transit import EncounterCarrier


class KillEncounterCarrier(EncounterCarrier[KillEncounter]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated KillEncounter or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [KillEncounter | KillEncounterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[KillEncounterBlueprint]

    Super Class:
        EncounterCarrier
    """
    
    def __init__(
            self,
            model: Optional[KillEncounter] | None = None,
            blueprint: Optional[KillEncounterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[KillEncounter]
            blueprint: Optional[KillEncounterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[KillEncounter | KillEncounterBlueprint]:
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
                isinstance(self._model, KillEncounter)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, KillEncounterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[KillEncounterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(KillEncounter, self._model)
        return KillEncounterBlueprint(
            id=model.id,
            victim=model.victim,
            attacker_maneuver=model.attacker_maneuver,
        )


