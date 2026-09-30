# src/domain/metadata/nulls/model/encounter/warning/group.py

"""
Module: domain.metadata.nulls.model.encounter.warning.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterNullGroup, EncounterWarning
from err import (
    EncounterWarningBlueprintNullException, EncounterWarningCarrierNullException,
    EncounterWarningNullException
)


class EncounterWarningNullGroup(EncounterNullGroup[EncounterWarning]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a EncounterWarning's integrity cycle.

    Attributes:
        model: EncounterWarningNullException
        carrier: EncounterWarningCarrierNullException
        blueprint: EncounterWarningBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[EncounterWarningNullException] | None = None,
            carrier: Optional[EncounterWarningCarrierNullException] | None = None,
            blueprint: Optional[EncounterWarningBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[EncounterWarningNullException]
            carrier: Optional[EncounterWarningCarrierNullException]
            blueprint: Optional[EncounterWarningBlueprintNullException]
        """
        super().__init__(
            model = model or EncounterWarningNullException(),
            carrier = carrier or EncounterWarningCarrierNullException(),
            blueprint = blueprint or EncounterWarningBlueprintNullException(),
        )
        
    @property
    def model(self) -> EncounterWarningNullException:
        return cast(EncounterWarningNullException, super().model)
    
    @property
    def carrier(self) -> EncounterWarningCarrierNullException:
        return cast(EncounterWarningCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> EncounterWarningBlueprintNullException:
        return cast(EncounterWarningBlueprintNullException, super().blueprint)