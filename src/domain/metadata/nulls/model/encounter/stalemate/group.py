# src/domain/metadata/nulls/model/encounter/stalemate/group.py

"""
Module: domain.metadata.nulls.model.encounter.stalemate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StalemateEncounter, EncounterNullGroup
from err import (
    StalemateEncounterBlueprintNullException, StalemateEncounterCarrierNullException,
    StalemateEncounterNullException
)


class StalemateEncounterNullGroup(EncounterNullGroup[StalemateEncounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a StalemateEncounter's integrity cycle.

    Attributes:
        model: StalemateEncounterNullException
        carrier: StalemateEncounterCarrierNullException
        blueprint: StalemateEncounterBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[StalemateEncounterNullException] | None = None,
            carrier: Optional[StalemateEncounterCarrierNullException] | None = None,
            blueprint: Optional[StalemateEncounterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[StalemateEncounterNullException]
            carrier: Optional[StalemateEncounterCarrierNullException]
            blueprint: Optional[StalemateEncounterBlueprintNullException]
        """
        super().__init__(
            model =model or StalemateEncounterNullException(),
            carrier =carrier or StalemateEncounterCarrierNullException(),
            blueprint =blueprint or StalemateEncounterBlueprintNullException(),
        )
        
    @property
    def model(self) -> StalemateEncounterNullException:
        return cast(StalemateEncounterNullException, super().model)
    
    @property
    def carrier(self) -> StalemateEncounterCarrierNullException:
        return cast(StalemateEncounterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> StalemateEncounterBlueprintNullException:
        return cast(StalemateEncounterBlueprintNullException, super().blueprint)