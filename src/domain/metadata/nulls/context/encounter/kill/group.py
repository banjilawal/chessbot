# src/domain/metadata/nulls/context/encounter/kill/group.py

"""
Module: domain.metadata.nulls.context.encounter.kill.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterContextNullGroup, KillEncounter
from err import (
    KillEncounterContextNullException, KillEncounterContextCarrierNullException,
    KillEncounterContextBlueprintNullException
)


class KillEncounterContextNullGroup(EncounterContextNullGroup[KillEncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a KillEncounter's integrity cycle.

    Attributes:
        model: KillEncounterContextNullException
        carrier: KillEncounterContextCarrierNullException
        blueprint: KillEncounterContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KillEncounterContextNullException] | None = None,
            carrier: Optional[KillEncounterContextCarrierNullException] | None = None,
            blueprint: Optional[KillEncounterContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KillEncounterContextNullException]
            carrier: Optional[KillEncounterContextCarrierNullException]
            blueprint: Optional[KillEncounterContextBlueprintNullException]
        """
        super().__init__(
            context =context or KillEncounterContextNullException(),
            carrier =carrier or KillEncounterContextCarrierNullException(),
            blueprint =blueprint or KillEncounterContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> KillEncounterContextNullException:
        return cast(KillEncounterContextNullException, super().model)
    
    @property
    def carrier(self) -> KillEncounterContextCarrierNullException:
        return cast(KillEncounterContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KillEncounterContextBlueprintNullException:
        return cast(KillEncounterContextBlueprintNullException, super().blueprint)