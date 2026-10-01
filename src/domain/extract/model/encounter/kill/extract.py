# src/domain/extract/model/encounter/kill.extract.py

"""
Module: domain.extract.model.encounter.kill.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    KillEncounter, KillEncounterBlueprint, EncounterPrimeExtract
)
from transit import KillEncounterCarrier


class KillEncounterPrimeExtract(EncounterPrimeExtract[KillEncounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for KillEncounterValidator.

    Attributes:
        carrier: KillEncounterCarrier
        blueprint: Optional[KillEncounterBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        EncounterPrimeExtract
    """

    def __init__(
            self,
            carrier: KillEncounterCarrier,
            blueprint: Optional[KillEncounterBlueprint] | None = None,
    ):
        """
        Args:
            carrier: KillEncounterCarrier
            blueprint: Optional[KillEncounterBlueprint[T]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> KillEncounterCarrier:
        return cast(KillEncounterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[KillEncounterBlueprint]:
        return cast(KillEncounterBlueprint, super().blueprint)