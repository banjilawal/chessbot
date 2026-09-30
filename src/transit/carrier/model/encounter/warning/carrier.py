# src/transit/carrier/model/encounter/warning/carrier.py

"""
Module: transit.carrier.model.encounter.warning.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarning, EncounterWarningBlueprint
from transit import EncounterCarrier


class EncounterWarningCarrier(EncounterCarrier[EncounterWarning]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated EncounterWarning or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Encounter | EncounterWarningBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[EncounterWarningBlueprint]

    Super Class:
        EncounterCarrier
    """
    
    def __init__(
            self,
            model: Optional[EncounterWarning] | None = None,
            blueprint: Optional[EncounterWarningBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterWarning]
            blueprint: Optional[EncounterWarningBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[EncounterWarning | EncounterWarningBlueprint]:
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
                isinstance(self._model, EncounterWarning)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, EncounterWarningBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[EncounterWarningBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(EncounterWarning, self._model)
        return EncounterWarningBlueprint(
            attacker_maneuver=model.attacker_maneuver,
            warning_recipient=model.warning_recipient,
            current_safe_square=model.current_safe_square,
        )


