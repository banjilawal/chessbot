# src/domain/extract/context/encounter/stalemate.extract.py

"""
Module: domain.extract.context.encounter.stalemate.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StalemateEncounter, StalemateEncounterContextBlueprint, EncounterContextPrimeExtract
from transit import StalemateEncounterContextCarrier


class StalemateEncounterContextPrimeExtract(EncounterContextPrimeExtract[StalemateEncounterContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for StalemateEncounterValidator.

    Attributes:
        contextCarrier: StalemateEncounterContextCarrier
        blueprint: Optional[StalemateEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextPrimeExtract
    """

    def __init__(
            self,
            reference: StalemateEncounterContextCarrier,
            blueprint: Optional[StalemateEncounterContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: StalemateEncounterContextCarrier
            blueprint: Optional[StalemateEncounterContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> StalemateEncounterContextCarrier:
        return cast(StalemateEncounterContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[StalemateEncounterContextBlueprint]:
        return cast(StalemateEncounterContextBlueprint, super().blueprint)