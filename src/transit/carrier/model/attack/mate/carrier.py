# src/transit/carrier/model/encounter/mate/carrier.py

"""
Module: transit.carrier.model.encounter.mate.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateEncounter, CheckmateEncounterBlueprint
from transit import EncounterCarrier


class CheckmateEncounterCarrier(EncounterCarrier[CheckmateEncounter]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CheckmateEncounter or its Blueprint across
            processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [CheckmateEncounter | CheckmateEncounterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CheckmateEncounterBlueprint]

    Super Class:
        EncounterCarrier
    """
    
    def __init__(
            self,
            model: Optional[CheckmateEncounter] | None = None,
            blueprint: Optional[CheckmateEncounterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CheckmateEncounter]
            blueprint: Optional[CheckmateEncounterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CheckmateEncounter | CheckmateEncounterBlueprint]:
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
                isinstance(self._model, CheckmateEncounter)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, CheckmateEncounterBlueprint)
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
    
    def extract_blueprint(self) -> Optional[CheckmateEncounterBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(CheckmateEncounter, self._model)
        return CheckmateEncounterBlueprint(
            id=model.id,
            team=model.team,
            position=model.position,
            readiness=model.readiness,
            formation=model.formation,
            checkmate=model.checkmate,
            deployment=model.deployment,
            home_square=model.home_square,
            check_warning=model.check_warning,
            previous_position=model.previous_position,
        )


