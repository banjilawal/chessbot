# src/domain/extract/model/encounter/stalemate.extract.py

"""
Module: domain.extract.model.encounter.stalemate.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StalemateEncounter, StalemateEncounterBlueprint, EncounterPrimeExtract
from transit import StalemateEncounterCarrier


class StalemateEncounterPrimeExtract(EncounterPrimeExtract[StalemateEncounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for StalemateEncounterValidator.

    Attributes:
        carrier: StalemateEncounterCarrier
        blueprint: Optional[StalemateEncounterBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        EncounterPrimeExtract
    """

    def __init__(
            self,
            carrier: StalemateEncounterCarrier,
            blueprint: Optional[StalemateEncounterBlueprint] | None = None,
    ):
        """
        Args:
            carrier: StalemateEncounterCarrier
            blueprint: Optional[StalemateEncounterBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> StalemateEncounterCarrier:
        return cast(StalemateEncounterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[StalemateEncounterBlueprint]:
        return cast(StalemateEncounterBlueprint, super().blueprint)