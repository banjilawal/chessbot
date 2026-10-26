# src/domain/metadata/nulls/context/encounter/checkmate/group.py

"""
Module: domain.metadata.nulls.context.encounter.checkmate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateEncounter, EncounterContextNullGroup
from err import (
    CheckmateEncounterContextBlueprintNullException, CheckmateEncounterContextCarrierNullException,
    CheckmateEncounterContextNullException
)


class CheckmateEncounterContextNullGroup(EncounterContextNullGroup[CheckmateEncounterContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a CheckmateEncounter's integrity cycle.

    Attributes:
        context: CheckmateEncounterContextNullException
        carrier: CheckmateEncounterContextCarrierNullException
        blueprint: CheckmateEncounterContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[CheckmateEncounterContextNullException] | None = None,
            carrier: Optional[CheckmateEncounterContextCarrierNullException] | None = None,
            blueprint: Optional[CheckmateEncounterContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[CheckmateEncounterContextNullException]
            carrier: Optional[CheckmateEncounterContextCarrierNullException]
            blueprint: Optional[CheckmateEncounterContextBlueprintNullException]
        """
        super().__init__(
            context =context or CheckmateEncounterContextNullException(),
            carrier =carrier or CheckmateEncounterContextCarrierNullException(),
            blueprint =blueprint or CheckmateEncounterContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> CheckmateEncounterContextNullException:
        return cast(CheckmateEncounterContextNullException, super().context)
    
    @property
    def carrier(self) -> CheckmateEncounterContextCarrierNullException:
        return cast(CheckmateEncounterContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CheckmateEncounterContextBlueprintNullException:
        return cast(CheckmateEncounterContextBlueprintNullException, super().blueprint)