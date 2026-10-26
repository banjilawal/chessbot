# src/domain/extract/context/encounter/kill.extract.py

"""
Module: domain.extract.context.encounter.kill.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    KillEncounter, KillEncounterContextBlueprint, EncounterContextPrimeExtract
)
from transit import KillEncounterContextCarrier


class KillEncounterContextPrimeExtract(EncounterContextPrimeExtract[KillEncounterContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for KillEncounterValidator.

    Attributes:
        contextCarrier: KillEncounterContextCarrier
        blueprint: Optional[KillEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextPrimeExtract
    """

    def __init__(
            self,
            reference: KillEncounterContextCarrier,
            blueprint: Optional[KillEncounterContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: KillEncounterContextCarrier
            blueprint: Optional[KillEncounterContextBlueprint[T]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> KillEncounterContextCarrier:
        return cast(KillEncounterContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[KillEncounterContextBlueprint]:
        return cast(KillEncounterContextBlueprint, super().blueprint)