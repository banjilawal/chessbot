# src/domain/extract/struct/encounter/checkmate.extract.py

"""
Module: domain.extract.struct.encounter.checkmate.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateEncounter, CheckmateEncounterBlueprint, EncounterPrimeExtract
from transit import CheckmateEncounterCarrier


class CheckmateEncounterPrimeExtract(EncounterPrimeExtract[CheckmateEncounter]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CheckmateEncounterValidator.

    Attributes:
        carrier: CheckmateEncounterCarrier
        blueprint: Optional[CheckmateEncounterBlueprint]

    Provides:

    Super Class:
        EncounterPrimeExtract
    """

    def __init__(
            self,
            carrier: CheckmateEncounterCarrier,
            blueprint: Optional[CheckmateEncounterBlueprint] | None = None,
    ):
        """
        Args:
            carrier: CheckmateEncounterCarrier
            blueprint: Optional[CheckmateEncounterBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> CheckmateEncounterCarrier:
        return cast(CheckmateEncounterCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[CheckmateEncounterBlueprint]:
        return cast(CheckmateEncounterBlueprint, super().blueprint)