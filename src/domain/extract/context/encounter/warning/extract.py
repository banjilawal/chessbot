# src/domain/extract/context/encounter/warning/extract.py

"""
Module: domain.extract.context.encounter.warning.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarning, EncounterWarningContextBlueprint, EncounterContextPrimeExtract
from transit import EncounterWarningContextCarrier


class EncounterWarningContextPrimeExtract(EncounterContextPrimeExtract[EncounterWarningContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for EncounterWarningValidator.

    Attributes:
        contextCarrier: EncounterWarningContextCarrier
        blueprint: Optional[EncounterWarningContextBlueprint]

    Provides:

    Super Class:
        EncounterContextPrimeExtract
    """

    def __init__(
            self,
            reference: EncounterWarningContextCarrier,
            blueprint: Optional[EncounterWarningContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: EncounterWarningContextCarrier
            blueprint: Optional[EncounterWarningContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> EncounterWarningContextCarrier:
        return cast(EncounterWarningContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[EncounterWarningContextBlueprint]:
        return cast(EncounterWarningContextBlueprint, super().blueprint)