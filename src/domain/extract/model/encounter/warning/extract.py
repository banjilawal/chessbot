# src/domain/extract/model/encounter/warning/extract.py

"""
Module: domain.extract.model.encounter.warning.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarning, EncounterWarningBlueprint, EncounterPrimeExtract
from transit import EncounterWarningCarrier


class EncounterWarningPrimeExtract(EncounterPrimeExtract[EncounterWarning]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for EncounterWarningValidator.

    Attributes:
        carrier: EncounterWarningCarrier
        blueprint: Optional[EncounterWarningBlueprint]

    Provides:

    Super Class:
        EncounterPrimeExtract
    """

    def __init__(
            self,
            reference: EncounterWarningCarrier,
            safe_blueprint: Optional[EncounterWarningBlueprint] | None = None,
    ):
        """
        Args:
            reference: EncounterWarningCarrier
            safe_blueprint: Optional[EncounterWarningBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> EncounterWarningCarrier:
        return cast(EncounterWarningCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[EncounterWarningBlueprint]:
        return cast(EncounterWarningBlueprint, super().blueprint)