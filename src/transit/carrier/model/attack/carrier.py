# src/transit/carrier/model/encounter/carrier.py

"""
Module: transit.carrier.model.encounter.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import Encounter, EncounterBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Encounter")

class EncounterCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Encounter or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Encounter|EncounterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[EncounterBlueprint]

    Super Class:
        ModelCarrier
    """
    _model: Optional[T]
    _blueprint: Optional[EncounterBlueprint]

    def __init__(
            self,
            model: Optional[Encounter] | None = None,
            blueprint: Optional[EncounterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Encounter]
            blueprint: Optional[EncounterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint

    @property
    def entity(self) -> Optional[Encounter | EncounterBlueprint]:
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
                isinstance(self._model, Encounter)
        )

    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, EncounterBlueprint)
        )

    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def not_consistent(self) -> bool:
        return self.size > 1

    @abstractmethod
    def extract_blueprint(self) -> Optional[EncounterBlueprint]:
        pass
    
    @property
    def is_king_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return blueprint.is_king_encounter_blueprint
    
    @property
    def is_pawn_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return blueprint.is_pawn_encounter_blueprint
    
    @property
    def is_combatant_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return (
                not self.is_king_encounter_carrier and
                not self.is_pawn_encounter_carrier
        )


