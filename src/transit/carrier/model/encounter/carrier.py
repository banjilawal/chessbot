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

from domain import (
    Blueprint, CheckmateEncounterBlueprint, Encounter, EncounterBlueprint,
    EncounterWarningBlueprint, KillEncounterBlueprint, StalemateEncounterBlueprint
)
from transit import ModelCarrier

T = TypeVar("T", bound="Encounter")

class EncounterCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Encounter or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [T | EncounterBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[EncounterBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[T]
    _blueprint: Optional[EncounterBlueprint[T]]
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[EncounterBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[EncounterBlueprint[T]]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[T | EncounterBlueprint[T]]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None
        )
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[EncounterBlueprint[T]]:
        pass
    
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


