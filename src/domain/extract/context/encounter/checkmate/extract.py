# src/domain/extract/context/encounter/checkmate.extract.py

"""
Module: domain.extract.context.encounter.checkmate.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateEncounter, CheckmateEncounterContextBlueprint, EncounterContextPrimeExtract
from transit import CheckmateEncounterContextCarrier


class CheckmateEncounterContextPrimeExtract(EncounterContextPrimeExtract[CheckmateEncounterContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for CheckmateEncounterValidator.

    Attributes:
        contextCarrier: CheckmateEncounterContextCarrier
        blueprint: Optional[CheckmateEncounterContextBlueprint]

    Provides:

    Super Class:
        EncounterContextPrimeExtract
    """

    def __init__(
            self,
            reference: CheckmateEncounterContextCarrier,
            blueprint: Optional[CheckmateEncounterContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: CheckmateEncounterContextCarrier
            blueprint: Optional[CheckmateEncounterContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> CheckmateEncounterContextCarrier:
        return cast(CheckmateEncounterContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CheckmateEncounterContextBlueprint]:
        return cast(CheckmateEncounterContextBlueprint, super().blueprint)