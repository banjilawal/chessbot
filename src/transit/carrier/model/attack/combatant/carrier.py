# src/transit/carrier/model/encounter/combatant/carrier.py

"""
Module: transit.carrier.model.encounter.combatant.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KillEncounter, CombatantEncounterBlueprint
from transit import EncounterCarrier


class CombatantEncounterCarrier(EncounterCarrier[KillEncounter]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CombatantEncounter or its Blueprint across
            processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [CombatantEncounter | CombatantEncounterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CombatantEncounterBlueprint]

    Super Class:
        EncounterCarrier
    """
    
    def __init__(
            self,
            model: Optional[KillEncounter] | None = None,
            blueprint: Optional[CombatantEncounterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CombatantEncounter]
            blueprint: Optional[CombatantEncounterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[KillEncounter | CombatantEncounterBlueprint]:
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
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, CombatantEncounterBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_over_capacity(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[CombatantEncounterBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(KillEncounter, self._model)
        return CombatantEncounterBlueprint(
            id=model.id,
            team=model.team,
            position=model.position,
            readiness=model.readiness,
            formation=model.formation,
            checkcombatant=model.checkcombatant,
            deployment=model.deployment,
            home_square=model.home_square,
            check_warning=model.check_warning,
            previous_position=model.previous_position,
        )


