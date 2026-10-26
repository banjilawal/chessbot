# src/domain/metadata/nulls/context/encounter/warning/group.py

"""
Module: domain.metadata.nulls.context.encounter.warning.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterContextNullGroup, EncounterWarning
from err import (
    EncounterWarningContextBlueprintNullException, EncounterWarningContextCarrierNullException,
    EncounterWarningContextNullException
)


class EncounterWarningContextNullGroup(EncounterContextNullGroup[EncounterWarningContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a EncounterWarning's integrity cycle.

    Attributes:
        context: EncounterWarningContextNullException
        carrier: EncounterWarningContextCarrierNullException
        blueprint: EncounterWarningContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[EncounterWarningContextNullException] | None = None,
            carrier: Optional[EncounterWarningContextCarrierNullException] | None = None,
            blueprint: Optional[EncounterWarningContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[EncounterWarningContextNullException]
            carrier: Optional[EncounterWarningContextCarrierNullException]
            blueprint: Optional[EncounterWarningContextBlueprintNullException]
        """
        super().__init__(
            context = context or EncounterWarningContextNullException(),
            carrier = carrier or EncounterWarningContextCarrierNullException(),
            blueprint = blueprint or EncounterWarningContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> EncounterWarningContextNullException:
        return cast(EncounterWarningContextNullException, super().context)
    
    @property
    def carrier(self) -> EncounterWarningContextCarrierNullException:
        return cast(EncounterWarningContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> EncounterWarningContextBlueprintNullException:
        return cast(EncounterWarningContextBlueprintNullException, super().blueprint)