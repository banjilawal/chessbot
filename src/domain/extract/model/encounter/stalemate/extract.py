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

    Super Class:
        EncounterPrimeExtract
    """

    def __init__(
            self,
            reference: StalemateEncounterCarrier,
            blueprint: Optional[StalemateEncounterBlueprint] | None = None,
    ):
        """
        Args:
            reference: StalemateEncounterCarrier
            blueprint: Optional[StalemateEncounterBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> StalemateEncounterCarrier:
        return cast(StalemateEncounterCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[StalemateEncounterBlueprint]:
        return cast(StalemateEncounterBlueprint, super().blueprint)