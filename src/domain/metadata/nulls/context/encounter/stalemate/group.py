# src/domain/metadata/nulls/context/encounter/stalemate/group.py

"""
Module: domain.metadata.nulls.context.encounter.stalemate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StalemateEncounter, EncounterContextNullGroup
from err import (
    StalemateEncounterContextBlueprintNullException, StalemateEncounterContextCarrierNullException,
    StalemateEncounterContextNullException
)


class StalemateEncounterContextNullGroup(EncounterContextNullGroup[StalemateEncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a StalemateEncounter's integrity cycle.

    Attributes:
        context: StalemateEncounterContextNullException
        carrier: StalemateEncounterContextCarrierNullException
        blueprint: StalemateEncounterContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[StalemateEncounterContextNullException] | None = None,
            carrier: Optional[StalemateEncounterContextCarrierNullException] | None = None,
            blueprint: Optional[StalemateEncounterContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[StalemateEncounterContextNullException]
            carrier: Optional[StalemateEncounterContextCarrierNullException]
            blueprint: Optional[StalemateEncounterContextBlueprintNullException]
        """
        super().__init__(
            context =context or StalemateEncounterContextNullException(),
            carrier =carrier or StalemateEncounterContextCarrierNullException(),
            blueprint =blueprint or StalemateEncounterContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> StalemateEncounterContextNullException:
        return cast(StalemateEncounterContextNullException, super().context)
    
    @property
    def carrier(self) -> StalemateEncounterContextCarrierNullException:
        return cast(StalemateEncounterContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> StalemateEncounterContextBlueprintNullException:
        return cast(StalemateEncounterContextBlueprintNullException, super().blueprint)