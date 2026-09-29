# src/transit/carrier/model/encounter/carrier.py

"""
Module: transit.carrier.model.encounter.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import (
    CheckmateEncounterBlueprint, Encounter, EncounterWarningBlueprint,
    KillEncounterBlueprint, StalemateEncounterBlueprint
)
from transit import ModelCarrier

T = TypeVar("T", bound="Encounter")

class EncounterCarrier(ModelCarrier[T], ABC, Generic[T]):
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
    def __init__(self):
        super().__init__()
    
    @property
    def is_checkmate_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, CheckmateEncounterBlueprint)
    
    @property
    def is_stalemate_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, StalemateEncounterBlueprint)
    
    @property
    def is_kill_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, KillEncounterBlueprint)
    
    @property
    def is_warning_encounter_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, EncounterWarningBlueprint)


