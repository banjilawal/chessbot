# src/domain/metadata/nulls/model/encounter/kill/group.py

"""
Module: domain.metadata.nulls.model.encounter.kill.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterNullGroup, KillEncounter
from err import (
    KillEncounterNullException, KillEncounterCarrierNullException,
    KillEncounterBlueprintNullException
)


class KillEncounterNullGroup(EncounterNullGroup[KillEncounter]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a KillEncounter's integrity cycle.

    Attributes:
        model: KillEncounterNullException
        carrier: KillEncounterCarrierNullException
        blueprint: KillEncounterBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KillEncounterNullException] | None = None,
            carrier: Optional[KillEncounterCarrierNullException] | None = None,
            blueprint: Optional[KillEncounterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KillEncounterNullException]
            carrier: Optional[KillEncounterCarrierNullException]
            blueprint: Optional[KillEncounterBlueprintNullException]
        """
        super().__init__(
            model =model or KillEncounterNullException(),
            carrier =carrier or KillEncounterCarrierNullException(),
            blueprint =blueprint or KillEncounterBlueprintNullException(),
        )
        
    @property
    def model(self) -> KillEncounterNullException:
        return cast(KillEncounterNullException, super().model)
    
    @property
    def carrier(self) -> KillEncounterCarrierNullException:
        return cast(KillEncounterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KillEncounterBlueprintNullException:
        return cast(KillEncounterBlueprintNullException, super().blueprint)